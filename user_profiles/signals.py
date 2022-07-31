from django.contrib.auth.models import User
from user_profiles.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, "__Created: ", created)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_profile_status(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(
            user_profile=instance,
            status_message=f"New user: {instance.user.username} "
        )
