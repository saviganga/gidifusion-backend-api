from django.db import models

from django.contrib.auth.models import AbstractUser
# from teams.models import Team
from .managers import MyUserManager
# Team model form teams app
from teams.models import Team

# Create your models here.

class MyUser(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True, max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_player = models.BooleanField()
    is_fan = models.BooleanField()

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return self.first_name


class Player(models.Model):

    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='players')
    # role = choices (coach, baller)

    def __str__(self):
        return self.profile.first_name
