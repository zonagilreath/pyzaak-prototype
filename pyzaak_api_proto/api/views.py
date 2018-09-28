from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    #TODO find a way to assign ownership to profile to check against
    #or figure out other way to limit permissions of authenticated users


class GameList(generics.ListAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class SideDeckDetail(generics.RetrieveUpdateAPIView):
    lookup_field = 'user'
    queryset = models.SideDeck.objects.all()
    serializer_class = serializers.SideDeckSerializer
