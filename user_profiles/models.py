from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.city}"


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_message = models.CharField(max_length=240)
    date_of_create = models.DateTimeField(auto_now_add=True)
    dete_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile}"
