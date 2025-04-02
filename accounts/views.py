from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'required username and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).first():
            return Response({'error': "already exist password"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

class LogoutView(generics.GenericAPIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'success logout'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)