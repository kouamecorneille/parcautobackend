from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(
        max_length=255, min_length=4)
    first_name = serializers.CharField(
        max_length=255, min_length=2
    )
    last_name = serializers.CharField(
        max_length=255, min_length=2
    )

    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), write_only=True)
    libelle_role = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'numero_telephone',
                  'role', 'libelle_role',"piece_identite","adresse"]

    def get_libelle_role(self, obj):
        return obj.role.libelle_role if obj.role else None

    def validate(self, attrs):
        email = attrs.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('l\'Email est deja utilisé')})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['numero_telephone'] = validated_data.get('username')
        user = CustomUser.objects.create_user(**validated_data)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, min_length=2
    )
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
   
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password']


class UserUpadateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'numero_telephone',"piece_identite","adresse"]



class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, required=True)
    new_password = serializers.CharField(max_length=128, required=True)



class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'numero_telephone', 'piece_identite', 'adresse', 'role']
