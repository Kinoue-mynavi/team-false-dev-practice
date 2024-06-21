<<<<<<< HEAD
from flask import render_template
from flask_app.__init__ import app
from flask_app.views.staff.common.staff_common import is_staff_login
from flask_app.models.functions.customer import read_customer_one


# アカウント情報表示
@app.route("/customer_info", methods=["GET", "POST"])
@is_staff_login
def customer_info():
    # 表示するレコードを指定する
    # customer = read_customer_one(session[logged_in_customer_id])
    customer = read_customer_one(1)

    if customer.customer_payment == "1":
        payment = "クレジットカード"
    
    elif customer.customer_payment == "2":
        payment = "PayPay"
    
    elif customer.customer_payment == "3":
        payment = "銀行振込"
    
    else:
        payment = "未選択"


    return render_template("/customer/mypage/manage_accont/info.html",
                customer_account = customer.customer_account,
                customer_password = customer.customer_password,
                customer_name = customer.customer_name,
                customer_zipcode = customer.customer_zipcode,
                customer_address = customer.customer_address,
                customer_phone = customer.customer_phone,
                customer_payment = payment)
=======
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


>>>>>>> develop
