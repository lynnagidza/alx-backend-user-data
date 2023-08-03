#!/usr/bin/env python3
""" Tasks 5 and 6 """
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    hashed_bytes = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_bytes


def is_valid(hashed_password: bytes, password: str) -> bool:
    """returns a boolean"""
    return bcrypt.checkpw(password.encode(), hashed_password)
