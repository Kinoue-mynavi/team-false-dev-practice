from operator import itemgetter
from flask import render_template, flash, request, redirect, session, url_for, Markup
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.event import create_event
from flask_app.models.functions.reservations import delete_reservation, param_reservation, read_reservation
from flask_app.views.customer.common.customer_common import is_customer_login

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

# 予約管理　list
@app.route("/customer_manage_reservation", methods=["GET", "POST"])
@is_customer_login

def customer_manage_reservation():
    tbl_reservation = read_reservation()
    reservation_param_list = sorted(param_reservation(tbl_reservation),
                                    key=itemgetter('event_date'))

    

    # 予約情報が1件も取得できなければ、エラーメッセージ表示
    if not reservation_param_list:
        flash(errorMessages.w01('予約情報'))
        
    return render_template("/customer/mypage/manage_ticket/confirm_cancel.html", reservation_param_list=reservation_param_list)
 
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
