from django.shortcuts import render
from rest_framework import viewsets
from .models import MyUser, Player
from .serializers import MyUserSerializer, PlayerSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()



class PlayerViewSet(viewsets.ModelViewSet):

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()