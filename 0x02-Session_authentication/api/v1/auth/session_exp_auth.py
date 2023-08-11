#!/usr/bin/env python3
""" Session Exp Auth
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Exp Auth class
    """

    def __init__(self):
        """ Init
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """ Create Session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID for Session ID
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        if 'created_at' not in self.user_id_by_session_id[session_id].keys():
            return None
        if 'user_id' not in self.user_id_by_session_id[session_id].keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']
        created_at = self.user_id_by_session_id[session_id]['created_at']
        session_duration = timedelta(seconds=self.session_duration)
        if created_at + session_duration < datetime.now():
            return None
        return self.user_id_by_session_id[session_id]['user_id']
