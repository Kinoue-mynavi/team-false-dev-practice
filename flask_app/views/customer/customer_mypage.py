from flask import render_template, redirect, session
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()
#ここにログインチェック関数のインポート


# マイページメニュー（トップページ）
@app.route("/mypage_mypage_top")
def mypage_mypage_top():
    return "<p>マイページTOP画面</p>"

#アカウント情報に遷移
@app.route("/mypage_manage_account")
def mypage_manage_account():
    if session["logged_in_customer"] == True:
        return render_template("/customer/mypage/manage_account/info.html")
    else:
        return redirect("/customer/auth/login.html")

#予約一覧に遷移
@app.route("/mypage_manage_ticket")
def mypage_manage_ticket():
    if session["logged_in_customer"] == True:
        return render_template("/customer/mypage/manage_ticket/list.html")
    else:
        return redirect("/customer/auth/login.html")

#退会に遷移
@app.route("/mypage_manage_unsubscribe")
def mypage_manage_unsubscribe():
    if session["logged_in_customer"] == True:
        return render_template("/customer/mypage/manage_unsubscribe/confirm.html")
    else:
        return redirect("/customer/auth/login.html")


#退会
@app.route("/mypage/manage_unsubscribe/confirm")
def display_confirmation():
    return render_template("/customer/mypage/manage_unsubscribe/confirm.html")



# チケット詳細 キャンセル確認に遷移
@app.route("/mypage/manage_ticket/confirm_cancel")
def confirm_cancel():
    if session["logged_in_customer"] == True:
        # チケット詳細を開いてキャンセル確認

        return render_template("/customer/mypage/manage_ticket/confirm_cancel.html")
    else:
        return redirect("/customer/auth/login.html")

# チケットキャンセル チケット一覧に遷移
@app.route("/mypage_manage_ticket")
def ticket_cancel_list():
    if session["logged_in_customer"] == True:
        # チケットキャンセルして一覧に戻る

        return render_template("/customer/mypage/manage_ticket/list.html")
    else:
        return redirect("/customer/auth/login.html")
