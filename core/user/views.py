from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from .handlers import UserHandler

class UserViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated]
    
    def get_profile(self,request,id):
        data,status = UserHandler.get_profile_by_id(id)
        return Response(data,status=status)