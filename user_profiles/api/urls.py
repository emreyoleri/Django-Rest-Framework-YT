from django.urls import path
from user_profiles.api import views as api_views

urlpatterns = [
    path("user-profiles/" , api_views.ProfilesList.as_view() , name="user-profiles")
]
