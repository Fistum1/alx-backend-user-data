#!/usr/bin/env python3
"""
It's encrypting the passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    It returns a salted, hashed password, which is a byte string
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    It validates the provided password matches the hashed password
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
