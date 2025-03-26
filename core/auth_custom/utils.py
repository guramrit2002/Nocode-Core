
class GoogleUtils:
    
    '''Google integration utilities'''
    
    @classmethod
    def get_login_url(client_id,redirect_uri):
        # login url where frontend will redirect
        return (
            f"https://accounts.google.com/o/oauth2/auth"
            f"?client_id={client_id}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=email%20profile"
        )
    