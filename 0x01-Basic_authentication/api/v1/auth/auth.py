#!/usr/bin/env python3
"""Authentication module for API"""
from flask import request
from typing import List, TypeVar, Optional


class Auth:
    """
    Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required to access path"""
        if not excluded_paths or not path:
            return True
        path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.strip("*")):
                return False
        return True

    def authorization_header(self, request=None) -> Optional[str]:
        """ Check for authorization header in request"""
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns user object"""
        return None
