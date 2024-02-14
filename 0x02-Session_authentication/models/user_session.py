#!/usr/bin/env python3
"""
It is a user session module
"""
from models.base import Base


class UserSession(Base):
    """
    It is a user Session Class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        It is a constructor Method
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id'
