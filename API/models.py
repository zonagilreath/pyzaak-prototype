from django.db import models
from django.contrib.auth.models import User
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
