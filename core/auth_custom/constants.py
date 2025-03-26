from django.conf import settings

CLIENT_ID = settings.SOCIALACCOUNT_PROVIDERS.get("google",{}).get("APP",{})\
    .get("client_id","")
REDIRECT_URI = settings.SOCIALACCOUNT_PROVIDERS.get("google",{}).get("APP",{})\
    .get("redirect_uri","")
SECRET = settings.SOCIALACCOUNT_PROVIDERS.get("google",{}).get("APP",{})\
    .get("secret","")
CAP_LETTERS = r"[A-Z]"
SMALL_LETTER = r"[a-z]"
ATLEAS_ONE_LETTER = r"\d"
ATLEAST_ONE_SPECIAL_LETTER = r"[@$!%*?&]"