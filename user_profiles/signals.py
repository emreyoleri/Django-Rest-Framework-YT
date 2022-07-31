from django.contrib.auth.models import User
from user_profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sernder, instance, created, ** kwargs):
    print(instance.username, "__Created: ", created)
    if created:
        Profile.objects.create(user=instance)
