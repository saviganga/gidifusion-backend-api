from django.db import models

# Create your models here.

class Team(models.Model):

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=50, unique = True)
    