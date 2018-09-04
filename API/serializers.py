from rest_framework import serializers


class ProfileSerializer(serlizers.ModelSerializer):
    class Meta:
        model = Profile
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
