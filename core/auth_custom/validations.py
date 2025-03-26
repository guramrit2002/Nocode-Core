import re
from .constants import *
from user.models import UserProfile

class RegisterValidations:
    '''Validation Logic for user registeration'''
    
    @staticmethod
    def __common_validations(user_creds):
        common_errors = {"username":[],"password":[],"confirm_password":[]}
        
        for cred in ["password","username"]:
            if len(user_creds.get(cred)) < 8:
                common_errors.get(cred).append(f"{cred} must be at least 8 "
                                            "characters long.")
            if not re.search(CAP_LETTERS, user_creds.get(cred)):
                common_errors.get(cred).append(f"{cred} must contain at least one "
                                    "uppercase letter.")
            if not re.search(SMALL_LETTER, user_creds.get(cred)):
                common_errors.get(cred).append(f"{cred} must contain at least one "
                                    "lowercase letter.")
            if not re.search(ATLEAS_ONE_LETTER, user_creds.get(cred)):
                common_errors.get(cred).append(f"{cred} must contain at least one "
                                    "digit.")
            if not re.search(ATLEAST_ONE_SPECIAL_LETTER, user_creds.get(cred)):
                common_errors.get(cred).append(f"{cred} must contain at least one "
                    "special character (@, $, !, %, *, ?, &).")
                
        return common_errors
    
    @staticmethod
    def __password_validations(user_creds):
        password_errors = []
        if user_creds.get("username") in user_creds.get("password"):
            password_errors.append("Password must not contain username")
        return password_errors
    
    @staticmethod
    def __username_validations(username):
        username_errors = []
        if UserProfile.objects.filter(username=username).exists():
            username_errors.append("Username is already taken")
        return []
    
    @staticmethod
    def __confirm_validations(user_creds):
        confirm_validations = []
        if user_creds.get("confirm_password") != user_creds.get("password"):
            confirm_validations.append("Passwords are not matching")
        return confirm_validations
    
    @classmethod
    def is_cred_valid(cls,user_creds):
        common_error = cls.__common_validations(user_creds)
        password_error = cls.__password_validations(user_creds)
        username_error = cls.__username_validations(user_creds)
        confirm_error = cls.__confirm_validations(user_creds)
        
        if len(username_error):
            common_error["username"] += username_error
        if len(password_error):
            common_error["password"] += password_error
        if len(confirm_error):
            common_error["confirm_password"] += confirm_error
            print(common_error)
        
        is_common_error = (len(password_error)
            + len(username_error)
            + len(common_error.get("username"))
            + len(common_error.get("password"))
            + len(common_error.get("confirm_password")))
        
        if not is_common_error:
            return False, user_creds
        
        return True, common_error