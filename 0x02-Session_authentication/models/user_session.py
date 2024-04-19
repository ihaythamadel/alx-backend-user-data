#!/usr/bin/env python3
"""User session"""
from models.base import Base


class UserSession(Base):
        """ session object """
        def __init__(self, *args: list, **kwargs: dict):
            """ Init UserSession"""
            super().__init__(*args, **kwargs)
            self.user_id = kwargs.get("user_id")
            self.session_id = kwargs.get("session_id", self.id)
