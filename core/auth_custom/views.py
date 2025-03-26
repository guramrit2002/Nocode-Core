import re
import json
import requests
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from .constants import CLIENT_ID, REDIRECT_URI
from .utils import GoogleUtils
from .handlers.google_handler import GoogleHandler
from .handlers.user_handler import AuthHandler
from .serializers import RegisterSerializer

class SocialLoginViewSet(ViewSet):
    
    permission_classes = [AllowAny]
    
    def get_google_login_url(self,request):
        adapter = GoogleOAuth2Adapter(request)
        provider = adapter.get_provider()
        login_url = GoogleUtils.get_login_url(CLIENT_ID, REDIRECT_URI)
        return Response({"login_url": login_url})

    def get_google_token(self,request):
        
        code = request.GET.get("code")
        
        if not code:
            return Response({"error": "No code provided by Google"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        token_info,status = GoogleHandler.google_token_api_call(code)
        if isinstance(token_info,str):
            token_info = json.loads(token_info)
        return Response(token_info,status=status)

class RegisterViewSet(ViewSet):
    
    def register(self,request):
        data, status = AuthHandler.user_registeration(request=request)
        return Response(data,status=status)

class LoginViewSet(ViewSet):
    
    def login(self, request):
        data, status = AuthHandler.user_login(request=request)
        return Response(data,status=status)