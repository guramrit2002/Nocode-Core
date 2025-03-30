import re
from rest_framework import serializers
from .constants import CAP_LETTERS, SMALL_LETTER, ATLEAS_ONE_LETTER,\
    ATLEAST_ONE_SPECIAL_LETTER
from .validations import RegisterValidations

class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=20,required=True)
    password = serializers.CharField(max_length=50,write_only=True,
                                    required=True)
    confirm_password = serializers.CharField(max_length=50,write_only=True,
                                    required=True)
        
    def validate(self,data):
        errors,data = RegisterValidations.is_cred_valid(user_creds=data)
        # if errors:
        #     raise serializers.ValidationError(data)
        print(data)
        return data

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=20,required=True)
    password = serializers.CharField(max_length=50,required=True)
    