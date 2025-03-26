from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    '''Additional fields for User Profile'''
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    account_status = models.CharField(
        max_length=20,
        choices=[("Active", "Active"), ("Banned", "Banned"), ("Pending", "Pending")],
        default="Active",
    )
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    medium = models.URLField(blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="userprofile_groups",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="userprofile_permissions",
        blank=True
    )
    
    USERNAME_FIELD = "username"  

    def __str__(self):
        return self.username + ' profile'
