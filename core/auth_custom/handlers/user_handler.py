from django.db import IntegrityError
from rest_framework import status
from ..serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from user.models import UserProfile

class AuthHandler:
    '''Handler for user related business logic'''
    
    @classmethod
    def user_registeration(cls, request):
        try:
            user_creds = request.data
            register_serializer = RegisterSerializer(data=user_creds)

            if register_serializer.is_valid():
                try:
                    user_creds.pop('confirm_password')  # Remove confirm password field
                    user = UserProfile.objects.create_user(**user_creds)
                    user.set_password(user_creds["password"])
                    user.save()

                    is_error, tokens = cls.get_login_user_token(user)
                    if not is_error:
                        return (
                            {"message": "User registration successful!", **tokens},
                            status.HTTP_200_OK,
                        )
                    else:
                        return {"errors": str(tokens)}, status.HTTP_400_BAD_REQUEST
                        
                except IntegrityError:
                    return (
                        {"error": "Username already exists. Please choose another one."},
                        status.HTTP_400_BAD_REQUEST,
                    )

            return register_serializer.errors, status.HTTP_400_BAD_REQUEST

        except Exception as exp:
            print(exp)
            return {"errors": str(exp)}, status.HTTP_400_BAD_REQUEST

    @staticmethod
    def get_login_user_token(user):
        try:
            refresh = RefreshToken.for_user(user)
            return False, {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        except Exception as e:
            print(e)
            return True, str(e)

    @classmethod
    def user_login(cls, request):
        try:
            login_serializer = LoginSerializer(data=request.data)

            if login_serializer.is_valid():
                user_creds = login_serializer.validated_data
                username = user_creds.get("username")
                password = user_creds.get("password")

                user = authenticate(username=username, password=password)
                print(user)
                
                if user:
                    is_error, tokens = cls.get_login_user_token(user)
                    if is_error:
                        return {"errors": tokens}, status.HTTP_401_UNAUTHORIZED
                    return tokens, status.HTTP_200_OK
                else:
                    return (
                        {"errors": "User credentials provided are not correct"},
                        status.HTTP_401_UNAUTHORIZED,
                    )

            elif login_serializer.errors:
                return {"error": login_serializer.errors}, status.HTTP_400_BAD_REQUEST

        except Exception as e:
            return {"errors": str(e)}, status.HTTP_401_UNAUTHORIZED
