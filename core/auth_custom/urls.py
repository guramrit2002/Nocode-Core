from django.urls import path
from auth_custom.views import RegisterViewSet, SocialLoginViewSet, LoginViewSet

urlpatterns = [
    path('register',RegisterViewSet.as_view({'post':'register'})),
    path('login',LoginViewSet.as_view({'post':'login'})),
    path('get_google_login_url',SocialLoginViewSet.as_view({'get':\
        'get_google_login_url'})),
    path('get_google_token',SocialLoginViewSet.as_view({"get":"get_google_token"}))
]
