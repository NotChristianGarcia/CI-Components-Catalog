from config import config
from flask import session
from tapipy.tapis import Tapis


def is_logged_in():
    """
    Check whether the current session contains a valid login;
    If so: return True, username, roles
    Otherwse: return False, None, None
    """
    if 'username' in session:
        return True, session['username'], session['roles']
    return False, None, None 


def add_user_to_session(username, token):
    """
    Add a user's identity and Tapis token to the session. 
    Also, look up users roles in Tapis and add those to the session.
    The list of roles are returned.
    """
    session['username'] = username
    session['token'] = token
    # also, look up user's roles
    t = Tapis(base_url=config['tapis_base_url'], access_token=token)
    try:
        result = t.sk.getUserRoles(user=username, tenant="icicle")
        session['roles'] = result.names
    except Exception as e:
        raise Exception(f"Error getting user's roles; debug: {e}")
    return result.names


def clear_session():
    """
    Remove all data on the session; this function is called on logout.
    """
    session.pop('username', None)
    session.pop('token', None)
    session.pop('roles', None)
