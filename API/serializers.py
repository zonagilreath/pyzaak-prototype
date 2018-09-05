from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            'rank',
            'total_xp',
            'games_played',
            'games_won',
            'joined'
            )
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = models.User
        fields = ('username', 'email', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        for tuple in profile_data.items():
            attr = tuple[0]
            val = tuple[1]
            setattr(profile, attr, val)
        profile.save()

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game