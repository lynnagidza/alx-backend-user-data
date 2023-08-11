#!/usr/bin/env python3
""" Session DB Auth """
from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Session DB Auth class
    """

    def create_session(self, user_id=None):
        """ Create Session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        new_user_session = UserSession(**session_dictionary)
        new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ User ID for Session ID
        """
        if session_id is None:
            return None
        user_session = UserSession.search({'session_id': session_id})
        if len(user_session) == 0:
            return None
        user_session = user_session[0]
        if self.session_duration <= 0:
            return user_session.user_id
        created_at = user_session.created_at
        session_duration = timedelta(seconds=self.session_duration)
        if created_at + session_duration < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """ Destroy Session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_session = UserSession.search({'session_id': session_id})
        if len(user_session) == 0:
            return False
        user_session = user_session[0]
        user_session.remove()
        return True
