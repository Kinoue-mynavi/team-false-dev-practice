from flask import render_template, redirect
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.sessions.customer import has_auth_session

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

# マイページメニュー（トップページ）
@app.route("/mypage_mypage_top")
def mypage_mypage_top():
    return "<p>マイページTOP画面</p>"

#アカウント情報に遷移
@app.route("/mypage_manage_account")
def mypage_manage_account():
    if has_auth_session():
        return render_template("/customer/mypage/manage_account/info.html")
    else:
        return redirect("/customer/auth/login.html")
    
#予約一覧に遷移
@app.route("/mypage_manage_ticket")
def mypage_manage_ticket():
    if has_auth_session():
        return render_template("/customer/mypage/manage_ticket/list.html")
    else:
        return redirect("/customer/auth/login.html")

#退会に遷移
@app.route("/mypage_manage_unsubscribe")
def mypage_manage_unsubscribe():
    if has_auth_session():
        return render_template("/customer/mypage/manage_unsubscribe/confirm.html")
    else:
        return redirect("/customer/auth/login.html")


#退会
@app.route("/mypage/manage_unsubscribe/confirm")
def display_confirmation():
    return render_template("/customer/mypage/manage_unsubscribe/confirm.html")


