from flask import render_template, redirect, session, request
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.ticket import read_ticket_one, ticket_seat_id_str
from flask_app.models.functions.customer import read_customer_one
from flask_app.models.functions.event import read_event_one

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
        # チケットid, イベントid, 席種, 料金, 受付状態
        ticket = read_ticket_one(get_ticket_id)

        # チケット座席種類
        # "s00": "席種を選択","s01": "特別席","s02": "一般席","s11": "S席",
        # "s12": "A席","s13": "B席","s14": "C席","s31": "内野席","s32": "外野席"
        seat_str = ticket_seat_id_str(ticket.ticket_seat_id)

        # 会員情報取得
        customer_id = session["logged_in_customer_id"]
        # 会員名, 郵便番号, 住所, 電話番号, 支払方法
        customer_info = read_customer_one(customer_id)

        # 支払方法
        # 0未選択 1クレカ 2Pay 3振込
        if customer_info.customer_payment== "0":
            customer_payment_str = "未選択"
        elif customer_info.customer_payment == "1":
            customer_payment_str = "クレジットカード"
        elif customer_info.customer_payment == "2":
            customer_payment_str = "PayPay"
        elif customer_info.customer_payment == "3":
            customer_payment_str = "銀行振込"

        # イベント情報
        # イベント名, 開催日, 開催場所, イベント概要
        event = read_event_one(ticket.event_id)

        return render_template("/customer/mypage/manage_ticket/confirm_cancel.html",
            event=event, customer_info=customer_info, ticket=ticket, customer_payment_str=customer_payment_str, seat_str=seat_str)
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