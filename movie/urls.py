from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView ,MovieViewSet,GenreViewSet,ActorViewSet,LanguageViewSet,CountryViewSet,IndustryViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet ,basename='movies')
router.register('language', LanguageViewSet ,basename='language')
router.register('genres', GenreViewSet ,basename='genres')
router.register('countries', CountryViewSet ,basename='countries')
router.register('actors', ActorViewSet ,basename='actors')
router.register('industry', IndustryViewSet ,basename='industry')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
 
    path('', include(router.urls)),
]