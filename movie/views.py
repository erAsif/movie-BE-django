from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializer import (loginSerializer, registerSerializer,industrySerializer, MovieCreateSerializer,MovieReadSerializer,languageSerilizer,genreSerializer,countrySerializer,actorSerializer)
from .models import User, UserToken ,Language,Movies,Genre,Country,Actor,Industry
from django.contrib.auth.models import User as DjangoUser  # Django's user
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = registerSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # 1. Try custom User login
            try:
                user = User.objects.get(userName=username)
                if user.check_password(password):
                    token_obj, _ = UserToken.objects.get_or_create(user=user)
                    return Response({
                        "message": "Custom User Login successful",
                        "userType": "custom",
                        "token": token_obj.token,
                        "user": {
                            "userName": user.userName,
                            "email": user.email,
                            "mobileNo": user.mobileNo,
                        }
                    })
            except User.DoesNotExist:
                pass

            # 2. Try Django superuser login
            django_user = authenticate(username=username, password=password)
            if django_user:
                token, _ = Token.objects.get_or_create(user=django_user)
                return Response({
                    "message": "Django Superuser Login successful",
                    "userType": "django",
                    "token": token.key,
                    "user": {
                        "username": django_user.username,
                        "email": django_user.email,
                        "is_superuser": django_user.is_superuser
                    }
                })

            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MovieReadSerializer
        return MovieCreateSerializer 

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = languageSerilizer    

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = genreSerializer    

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = countrySerializer    

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = actorSerializer
    
class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = industrySerializer