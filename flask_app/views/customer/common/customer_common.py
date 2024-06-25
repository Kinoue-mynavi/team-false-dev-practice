from functools import wraps
from flask import redirect, session, url_for
from flask_app.models.functions.customer import read_customer_one
from flask_app.models.sessions.customer import has_auth_session


# ログイン認証のデコレータ
def is_customer_login(view):
    @wraps(view)
    def inner(*args, **kwargs):
        # 会員としてログインしていない場合は会員ログインページに遷移させる
        if not has_auth_session():
            return redirect(url_for("customer_customer_login"))
        return view(*args, **kwargs)
    return inner
