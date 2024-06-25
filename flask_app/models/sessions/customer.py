from flask import session

# ログイン状態

CUSTOMER_SESSION_FLAG = "logged_in_customer"

def create_auth_session():
    session[CUSTOMER_SESSION_FLAG] = True

def delete_auth_session():
    session.pop(CUSTOMER_SESSION_FLAG)

def has_auth_session() -> bool:
    return session.get('logged_in_customer', None) or False
