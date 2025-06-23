from django.contrib import admin
from .models import User, Genre, Language, Country, Actor, Industry, Movies

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName', 'email', 'mobileNo']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year']
    search_fields = ['title', 'description']
    list_filter = ['release_year', 'languages', 'genres', 'industries']
    filter_horizontal = ['genres', 'languages', 'countries', 'industries']
