from allauth.account import adapter
from django.db import models
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token

from .models import MyUser, Player
from django.contrib.auth import get_user_model

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password', 'is_player', 'is_fan')


class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_player = serializers.BooleanField()
    is_fan = serializers.BooleanField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password', 'is_player', 'is_fan']

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'is_player': self.validated_data.get('is_player', ''),
            'is_fan': self.validated_data.get('is_fan', '')
        }

    def save(self, request):
        
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_player = self.cleaned_data.get('is_player')
        user.is_fan = self.cleaned_data.get('is_fan')
        #user.password = self.cleaned_data.get('password1')
        user.save() 
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):

    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):

        serializer_data = MyUserSerializer(obj.user).data
        is_player = serializer_data.get('is_player')
        is_fan = serializer_data.get('is_fan')

        return {
            'is_player': is_player,
            'is_fan': is_fan,
        }



class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('profile', 'team',)
