<<<<<<< HEAD
"""Modules of project"""
from functools import wraps
from flask import session, redirect


def usd(value):
    """Format value as USD."""
    if value >= 0:
        return f"${value:,.2f}"
    else:
        value = -1 * value
        return f"(${value:,.2f})"


def login_required(f):
    """ Decorate routes to require login """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
=======
"""Modules of project"""
from functools import wraps
from flask import session, redirect


def usd(value):
    """Format value as USD."""
    if value >= 0:
        return f"${value:,.2f}"
    else:
        value = -1 * value
        return f"(${value:,.2f})"


def login_required(f):
    """ Decorate routes to require login """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
>>>>>>> 0db0c6166abf08ea6e6a4e7798b880dc2933653d
