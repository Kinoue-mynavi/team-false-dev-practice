from flask import render_template, redirect, session, request
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.ticket import read_ticket_event_id, read_ticket_one, read_ticket_one_dict
from flask_app.models.functions.customer import read_customer_one, read_customer_one_dict
from flask_app.models.functions.event import read_event_one, read_event_one_dict

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
        # ticket_id = request.form.get('ticket_id')
        # デバック用
        get_ticket_id = 1

        # チケット情報取得
        ticket = read_ticket_one_dict(get_ticket_id)
        # チケットid, イベントid, 席種, 料金, 受付状態

        ticket_id = ticket["ticket_id"]
        event_id = ticket["event_id"]
        ticket_seat_id = ticket["ticket_seat_id"]
        ticket_price = ticket["ticket_price"]
        ticket_accept = ticket["ticket_accept"]

        # 会員情報取得
        customer_id = session["logged_in_customer_id"]
        customer_info = read_customer_one_dict(customer_id)
        # 会員名, 郵便番号, 住所, 電話番号, 支払方法
        customer_name = customer_info["customer_name"]
        customer_zipcode = customer_info["customer_zipcode"]
        customer_address = customer_info["customer_address"]
        customer_phone = customer_info["customer_phone"]
        customer_payment = customer_info["customer_payment"]

        # イベント情報
        event = read_event_one_dict(event_id)
        # イベント名, 開催日, 開催場所, イベント概要
        event_name = event["event_name"]
        event_days = event["event_date"]
        event_place = event["event_place"]
        event_overview = event["event_overview"]

        return render_template("/customer/mypage/manage_ticket/confirm_cancel.html",
            ticket_id=ticket_id, event_id=event_id, ticket_seat_id=ticket_seat_id, ticket_price=ticket_price, ticket_accept=ticket_accept,
            customer_name=customer_name, customer_zipcode=customer_zipcode, customer_address=customer_address, customer_phone=customer_phone, customer_payment=customer_payment,
            event_name=event_name, event_days=event_days, event_place=event_place, event_overview=event_overview)
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
