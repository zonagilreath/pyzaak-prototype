from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ProfileSerializer(serlizers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            'rank',
            'total_xp',
            'games_played',
            'games_won',
            'joined'
            )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username',)
