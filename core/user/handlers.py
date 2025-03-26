from .models import UserProfile
from rest_framework import status


class UserHandler:
    
    @classmethod
    def get_profile_by_id(cls,user_id):
        user = UserProfile.objects.filter(id = user_id).values()
        return user, status.HTTP_200_OK
    