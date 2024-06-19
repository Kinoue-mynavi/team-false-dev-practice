from flask import render_template, flash, request, redirect, session
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.customer import read_customer_customer_account
from flask_app.views.customer.common.customer_common import is_customer_login

# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()


#会員ログイン
@app.route("/customer_customer_login", methods=["GET", "POST"])
def customer_customer_login():
    return render_template("/customer/auth/login.html")


# 会員ログイン処理
@app.route("/login_customer", methods=["POST"])
def login_customer():
    isLoginError = False

    customer_account = request.form.get("customer_account")
    customer_password = request.form.get("customer_password")

    # アカウント名とパスワードが提供されているか確認
    if not customer_account or not customer_password:
        flash(errorMessages.w02('アカウント名またはパスワード'))
        return render_template("/customer/auth/login.html")
    
    customer_array = read_customer_customer_account(
        request.form["customer_account"])
    
    # 会員アカウントが存在するかチェック
    if len(customer_array) == 0:
        flash(errorMessages.w04('アカウント名'))
        isLoginError = True
    
    # パスワードが一致するかチェック
    customer = customer_array[0]
    if request.form["customer_password"] != customer.customer_password:
        flash(errorMessages.w04('アカウント名'))
        isLoginError = True

    # エラーがあればログインページに遷移
    if isLoginError:
        return render_template("/customer/auth/login.html")

    else:
        # login処理を実行する
        session["logged_in_customer"] = True
        session["logged_in_customer_account"] = customer.customer_account
        session["logged_in_customer_id"] = customer.customer_id
        session["logged_in_customer_name"] = customer.customer_name
        flash(infoMessages.i05())
        return redirect("/customer_top")