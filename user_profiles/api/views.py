from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user_profiles.models import Profile
from user_profiles.api.serializers import ProfileSerializer

class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
