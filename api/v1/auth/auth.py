from flask import request
from typing import List, TypeVar

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
            require path
        '''
        if path is None or excluded_paths is None:
            return True
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path in excluded_paths:
            return False
        return True
    
    def authorization_header(self, request=None) -> str:
        '''
            header
        '''
        if request is None:
            return None
        return request.headers.get("Authorization", None)
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
            current_user
        """
        return None