from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.views import APIView
from .models import CustomUser, Role
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, LoginSerializer, PasswordChangeSerializer,ClientProfileSerializer, UserUpadateSerializer,RoleSerializer
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")  # type: ignore

            serializer = UserSerializer(user)

            data = {
                'user': serializer.data,
                'token': auth_token
            }
            return Response(data, status=status.HTTP_200_OK)

            # Reponses

        return Response({'detail': 'Informations invalides'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        auth.logout(request)
        return Response({'detail': 'Déconnexion réussie'}, status=status.HTTP_200_OK)

class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpadateSerializer


class PasswordChangeView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data.get("old_password")
            new_password = serializer.validated_data.get("new_password")

            if not user.check_password(old_password):
                return Response({"error": "Le mot de passe actuel est incorrect."}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({"success": "Le mot de passe a été changé avec succès."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientProfileView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.use

    
class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
