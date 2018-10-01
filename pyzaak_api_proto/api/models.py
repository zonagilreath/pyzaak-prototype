from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    RANK_CHOICES = (
            (1, 'Mark'),
            (2, 'Novice'),
            (3, 'Hustler'),
            (4, 'Sharp'),
            (5, 'Force User')
        )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
        )
    total_xp = models.IntegerField(default=0)
    rank = models.IntegerField(choices=RANK_CHOICES, default=0)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    location = models.CharField(max_length=30, blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images/')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class SideDeck(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='side_deck'
        )
    plus_1 = models.IntegerField(default=1)
    minus_1 = models.IntegerField(default=1)
    bival_1 = models.IntegerField(default=0)
    plus_2 = models.IntegerField(default=1)
    minus_2 = models.IntegerField(default=1)
    bival_2 = models.IntegerField(default=0)
    plus_3 = models.IntegerField(default=0)
    minus_3 = models.IntegerField(default=0)
    bival_3 = models.IntegerField(default=0)
    plus_4 = models.IntegerField(default=0)
    minus_4 = models.IntegerField(default=0)
    bival_4 = models.IntegerField(default=0)
    plus_5 = models.IntegerField(default=0)
    minus_5 = models.IntegerField(default=0)
    bival_5 = models.IntegerField(default=0)
    plus_6 = models.IntegerField(default=0)
    minus_6 = models.IntegerField(default=0)
    bival_6 = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_side_deck(sender, instance, created, **kwargs):
    if created:
        SideDeck.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_side_deck(sender, instance, **kwargs):
    instance.side_deck.save()


@receiver(post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='EndUser')
        instance.groups.add(group)
        instance.save()


class Game(models.Model):
    finished_at = models.DateTimeField(auto_now_add=True)
    user_1 = models.ForeignKey(
            User,
            on_delete='PROTECT',
            related_name='user_1',
            )
    user_2 = models.ForeignKey(
        User,
        on_delete='PROTECT',
        related_name='user_2'
        )
    user_1_rank = models.IntegerField(choices=Profile.RANK_CHOICES)
    user_2_rank = models.IntegerField(choices=Profile.RANK_CHOICES)
    winner = models.ForeignKey(
        User,
        on_delete='PROTECT',
        related_name='winner')
    user_1_xp_delta = models.IntegerField()
    user_2_xp_delta = models.IntegerField()
