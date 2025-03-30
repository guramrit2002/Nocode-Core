import requests
from django.conf import settings
from ..constants import CLIENT_ID, REDIRECT_URI, SECRET

class GoogleHandler:
    '''Buisness Logic for Google Authentication APIs'''
    @classmethod
    def google_token_api_call(cls,code):
        payload = {
        "client_id": CLIENT_ID,
        "client_secret": SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        }
        response = requests.post(settings.TOKEN_API, data=payload)
        return response.text, response.status_code