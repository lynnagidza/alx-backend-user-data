#!/usr/bin/env python3
""" Advanced Task Main Module """
from flask import request

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """ Register User """
    endpoint = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = request.post(endpoint, data=data)

    assert response.status_code == 200, "Failed to register user:\
        {response.content}"
    print("User registered successfully.")


def log_in_wrong_password(email: str, password: str) -> None:
    """ Log in Wrong Password """


def log_in(email: str, password: str) -> str:
    """ Log in """
    return ""


def profile_unlogged() -> None:
    """ Profile Unlogged """


def profile_logged(session_id: str) -> None:
    """ Profile Logged """


def log_out(session_id: str) -> None:
    """ Log out """
    pass


def reset_password_token(email: str) -> str:
    """ Reset Password Token """
    return ""


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update Password """
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
