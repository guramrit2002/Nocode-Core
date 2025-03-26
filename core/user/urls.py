from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('profile/<int:id>',UserViewSet.as_view({'get':'get_profile'}))
]