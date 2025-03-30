from .models import UserProfile
from rest_framework import status

class UserUtils:
    
    @classmethod
    def get_user_by_id(cls,user_id):
        try:
            user = UserProfile.objects.filter(id = user_id)
            return user, status.HTTP_200_OK
        except user.DoesNotExist:
            return user, status.HTTP_404_NOT_FOUND
        except Exception as e:
            return str(e), status.HTTP_400_BAD_REQUEST
    
    @classmethod
    def change_password_by_id(cls,user,new_password):
        user.set_password(new_password)
        user.save()
        return user