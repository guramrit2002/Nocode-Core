from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .handlers import UserHandler

class UserViewSet(ViewSet):
    
    @permission_classes([IsAuthenticated])
    def get_profile(self,request,id):
        data,status = UserHandler.get_profile_handler(user_id=id)
        return Response(data, status=status)
    
    def forget_password(self,request,id):
        data,status = UserHandler.forget_password_handler(\
            user_id=id,new_password=request.data.get("new_password"))
        print(status)
        return Response(data, status=status)
