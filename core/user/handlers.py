from rest_framework import status
from .utils import UserUtils
from .serializers import UserSerializer

class UserHandler:
    
    @classmethod
    def get_profile_handler(cls,user_id):
        try:
            user, profile_status = UserUtils.get_user_by_id(user_id=user_id)
            
            if profile_status == status.HTTP_200_OK:
                return user.values(), status.HTTP_200_OK
            return
        except Exception as e:
            return str(e), status.HTTP_400_BAD_REQUEST
    
    @classmethod
    def forget_password_handler(cls,user_id,new_password):
        try:
            user, profile_status = UserUtils.get_user_by_id(user_id=user_id)
            if profile_status == status.HTTP_200_OK:
                
                password_change = UserUtils.change_password_by_id\
                    (user=user.first(),new_password=new_password)
                    
                return ({"message":"Password is changed.","user":user.values()},
                        status.HTTP_200_OK)
        except Exception as e:
            return {"errors":str(e)}, status.HTTP_400_BAD_REQUEST