#!/usr/bin/env python3
"""Session Auth class"""
from datetime import datetime, timedelta
from typing import Union

from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """DB Session Authentication implementation"""
    def create_session(self, user_id=None) -> Union[str, None]:
        """Create session id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = super().create_session(user_id)
        if session_id:
            kwargs = {'user_id': user_id, 'session_id': session_id}
            new_user_session = UserSession(**kwargs)
            new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None) -> Union[str, None]:
        """get user id """
        users_session = UserSession.search({'session_id': session_id})
        if users_session != []:
            if not (timedelta(seconds=self.session_duration) +
                    users_session[0].created_at <= datetime.now()):
                return users_session[0].user_id
        return None

    def destroy_session(self, request=None) -> bool:
        """deletes the user session """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if self.user_id_for_session_id(session_id) is None:
            return False
        usersession = UserSession.search({'session_id': session_id})
        if usersession != []:
            usersession[0].remove()
            return True
        return False
