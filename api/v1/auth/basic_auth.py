from auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User

class BasicAuth(Auth):
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode()
        except Exception:
            return None
         
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        
        return decoded_base64_authorization_header.split(":")

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        header = self.authorization_header(request)
        if header is None:
            return None
        exctracted = self.extract_base64_authorization_header(header)
        if exctracted is None:
            return None
        decoded = self.decode_base64_authorization_header(exctracted)
        if decoded is None:
            return None
        email, pwd = self.extract_user_credentials(decoded)
        if not emauk or not pwd:
            return None
        user = self.user_object_from_credentials(email, pwd)
    
        return user