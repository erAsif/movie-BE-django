from django.db import models
from django.contrib.auth.hashers import check_password
import secrets


class User(models.Model):
    userName = models.CharField(unique=True, max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Store hashed password
    mobileNo = models.CharField(max_length=15)

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.userName
    
class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, unique=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_hex(20)
        return super().save(*args, **kwargs)
    
class Genre(models.Model):
    name = models.CharField(unique=True , max_length=20)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(unique=True , max_length=20)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(unique=True , max_length=20)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(unique=True , max_length=20)

    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name = models.CharField(unique=True , max_length=20)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(unique=True, max_length=100)
    genres = models.ManyToManyField('Genre')
    languages = models.ManyToManyField('Language')
    countries = models.ManyToManyField('Country')
    industries = models.ManyToManyField('Industry')
    description = models.TextField(max_length=1000, default='No description available')
    release_year = models.DateField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    