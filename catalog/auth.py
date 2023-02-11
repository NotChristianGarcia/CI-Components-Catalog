from flask import session


def is_logged_in():
    """
    Check whether the current session contains a valid login;
    If so: return True, username
    Otherwse: return False, None
    """
    if 'username' in session:
        return True, session['username']
    return False, None 


def add_user_to_session(username, token):
    """
    Add a user's identity and Tapis token to the session.
    """
    session['username'] = username
    session['token'] = token


def clear_session():
    session.pop('username', None)
    session.pop('token', None)
