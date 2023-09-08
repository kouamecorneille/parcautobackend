from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Personnalisez la réponse ici si nécessaire
            user = self.user
            token = response.data['token']
            return Response({
                'token': token,
                'user': user,
            })
        return response
