from django.shortcuts import render

from rest_framework import serializers, viewsets
from .models import Team
from .serializers import TeamSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):

    serializer_class = TeamSerializer
    queryset = Team.objects.all()