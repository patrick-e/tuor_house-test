from django.db import models

# Create your models here.

class UserSingIn(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        app_label = 'backend'

class UserSignUp(models.Model):
    nome = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        app_label = 'backend'


