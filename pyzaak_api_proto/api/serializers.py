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
            'joined',
            'location'
            )
        depth = 1
        extra_kwargs = {
            'rank': {'read_only': True},
            'total_xp': {'read_only': True},
            'games_played': {'read_only': True},
            'games_won': {'read_only': True},
            'joined': {'read_only': True},
            'location': {'read_only': False}
        }


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
    user_1_name = serializers.SerializerMethodField()
    user_2_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Game
        fields = (
            'finished_at',
            'user_1_name',
            'user_1_rank',
            'user_2_name',
            'user_2_rank',
            'winner',
            'user_1_xp_delta',
            'user_2_xp_delta',
            )

    def get_user_1_name(self, obj):
        return obj.user_1.username

    def get_user_2_name(self, obj):
        return obj.user_2.username


class SideDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SideDeck
        fields = '__all__'
