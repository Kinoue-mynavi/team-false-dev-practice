from operator import itemgetter
from flask import render_template, flash, request, redirect, session, url_for, Markup
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.reservations import param_reservation
from flask import render_template, flash, request, redirect, session, url_for
from flask import render_template, redirect, session
from flask_app.models.sessions.customer import has_auth_session
from flask_app.models.functions.ticket import read_ticket_one, ticket_seat_id_str, delete_ticket
from flask_app.models.functions.customer import read_customer_one, update_customer
from flask_app.models.functions.event import read_event_one
from flask_app.views.customer.common.customer_common import is_customer_login
from flask_app.models.functions.reservations import param_reservation, read_reservation_customer_id
from operator import itemgetter
from datetime import datetime
from flask_app.models.functions.review import create_review_script


# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()


# 予約管理　list
@app.route("/customer/manage_ticket/ticket_list", methods=["GET", "POST"])
@is_customer_login
def mypage_manage_ticket():
    # customer_id,ticket_id を取得
    customer_id = session.get('logged_in_customer_id')
    ticket_id = session.get('ticket_id')

    # customer_id を引数として渡す
    tbl_reservation = read_reservation_customer_id(customer_id)
    reservation_param_list = sorted(param_reservation(tbl_reservation), key=itemgetter('event_date'))

    # 予約情報が1件も取得できなければ、エラーメッセージ表示
    if not reservation_param_list:
        flash(errorMessages.w01('予約情報'))

    return render_template("/customer/mypage/manage_ticket/list.html",
        reservation_param_list = reservation_param_list,ticket_id = ticket_id)
    #ここにログインチェック関数のインポート

# アカウント情報表示
@app.route("/customer/manage_customer/customer_info", methods=["GET", "POST"])
def customer_info():
    if session["logged_in_customer"] == True:
        # 表示するレコードを指定する
        customer = read_customer_one(session["logged_in_customer_id"])

        if customer.customer_payment == "1":
            payment = "クレジットカード"
        elif customer.customer_payment == "2":
            payment = "PayPay"
        elif customer.customer_payment == "3":
            payment = "銀行振込"
        else:
            payment = "未選択"

        return render_template("/customer/mypage/manage_account/info.html",
            customer_account = customer.customer_account,
            customer_password = customer.customer_password,
            customer_name = customer.customer_name,
            customer_zipcode = customer.customer_zipcode,
            customer_address = customer.customer_address,
            customer_phone = customer.customer_phone,
            customer_payment = payment)
    else:
        return redirect("/customer/auth/login")


# マイページメニュー（トップページ）
@app.route("/customer/mypage_top")
def mypage_mypage_top():
    if session["logged_in_customer"] == True:
        return render_template("/customer/mypage/mypage_top.html")
    else:
        return redirect("/customer/auth/login")


#アカウント情報に遷移
@app.route("/mypage_manage_account")
def mypage_manage_account():
    if has_auth_session():
        return render_template("/customer/mypage/manage_account/info.html")
    else:
        return redirect("/customer/auth/login")


# #予約一覧に遷移
# @app.route("/customer/manage_ticket/ticket_list")
# def mypage_manage_ticket():
#     if has_auth_session():
#         return render_template("/customer/mypage/manage_ticket/list.html", mst_tickets=displayed_tickets, pagination=pagination)
#     else:
#         return redirect("/customer/auth/login.html")


#退会に遷移
@app.route("/customer/manage_unsubscribe/confirm")
def mypage_manage_unsubscribe():
    if has_auth_session():
        return render_template("/customer/mypage/manage_unsubscribe/confirm.html")
    else:
        return redirect("/customer/auth/login")


#退会
@app.route("/mypage/manage_unsubscribe/confirm")
def display_confirmation():
    if session["logged_in_customer"] == True:
        return render_template("/customer/mypage/manage_unsubscribe/confirm.html")
    else:
        return redirect("/customer/auth/login")


# チケット詳細 キャンセル確認に遷移
@app.route("/mypage/manage_ticket/confirm_cancel")
def confirm_cancel():
    if session["logged_in_customer"] == True:
        # チケット詳細を開いてキャンセル確認
        # get_ticket_id = request.form.get('ticket_id')
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

        # レビューボタンとキャンセルボタンの切り替え処理
        # フラグ trueで未開催 falseで開催済み
        event_future_flag = True
        event_date = event.event_date
        event_date = datetime.strptime(event_date, "%Y/%m/%d")
        # イベントの日時と今日の日時の比較
        if event_date >= datetime.now():
            event_future_flag = True
        elif event_date < datetime.now():
            event_future_flag = False

        return render_template("/customer/mypage/manage_ticket/confirm_cancel.html",
            event=event, customer_info=customer_info, ticket=ticket,
            customer_payment_str=customer_payment_str, seat_str=seat_str, event_future_flag=event_future_flag)
    else:
        return redirect("/customer/auth/login")


# チケットキャンセル チケット一覧に遷移
@app.route("/mypage_manage_ticket", methods=["POST"])
def ticket_cancel_list():
    if session["logged_in_customer"] == True:
        # チケットキャンセルして一覧に戻る
        ticket_id = request.form["ticket_id"]

        # チケット削除
        delete_ticket(ticket_id)
        flash(infoMessages.i03("予約情報"))

        return render_template("/customer/mypage/manage_ticket/list.html")
    else:
        return redirect("/customer/auth/login")

# レビュー画面に遷移
@app.route("/mypage_review", methods=["POST"])
def review():
    if session["logged_in_customer"] == True:
        # レビュー画面
        # チケットid取得
        # チケット情報:チケットid, イベントid, 席種, 料金, 受付状態
        ticket_id = request.form["ticket_id"]
        ticket = read_ticket_one(ticket_id)
        # イベント情報:イベント名, 開催日, 開催場所, イベント概要
        event = read_event_one(ticket.event_id)

        return render_template("/customer/mypage/manage_ticket/review.html", event=event, ticket_id=ticket_id)
    else:
        return redirect("/customer/auth/login")

# レビューをDBに追加 チケット一覧に遷移
@app.route("/mypage_manage_review", methods=["POST"])
def ticket_review_confirm():
    if session["logged_in_customer"] == True:
        # レビューの受け取り
        review_number = request.form["review_number"]
        review_title = request.form["review_title"]
        review_comment = request.form["review_comment"]

        # チケットid取得
        # チケット情報:チケットid, イベントid, 席種, 料金, 受付状態
        ticket_id = request.form["ticket_id"]
        ticket = read_ticket_one(ticket_id)

        # 会員情報取得
        customer_id = session["logged_in_customer_id"]

        # レビュー情報を辞書型に格納
        reviews = {"event_id": ticket.event_id, "customer_id": customer_id, "review_score": review_number,
            "review_title": review_title, "review_comment": review_comment}

        # レビューのDB追加
        create_review_script(reviews)

        return render_template("/customer/mypage/manage_ticket/list.html")
    else:
        return redirect("/customer/auth/login")

#アカウント情報変更に遷移
@app.route("/mypage_manage_account/edit")
def mypage_manage_account_edit():
    if session["logged_in_customer"] == True:
        # 会員情報の取得
        customer = read_customer_one(session["logged_in_customer_id"])

        return render_template("/customer/mypage/manage_account/edit_info.html",
            customer_account=customer.customer_account,
            customer_password=customer.customer_password,
            customer_name=customer.customer_name,
            customer_zipcode=customer.customer_zipcode,
            customer_address=customer.customer_address,
            customer_phone=customer.customer_phone,
            customer_payment=customer.customer_payment)
    else:
        return redirect("/customer/auth/login")


#アカウント情報変更画面
@app.route("/mypage_manage_account/update", methods=['POST', 'GET'])
def mypage_manage_account_update():
    if session["logged_in_customer"] == True:
        # バリデーションフラグ
        isValidateError = False

        # フォームから送信されたデータを受け取る
        # デバック用
        customer_account = request.form.get('customer_account')
        customer_password = request.form.get('customer_password')
        customer_name = request.form.get('customer_name')
        customer_zipcode = request.form.get('customer_zipcode')
        customer_address = request.form.get('customer_address')
        customer_phone = request.form.get('customer_phone')
        customer_payment = request.form.get('customer_payment')

        # バリデーションチェック
        # 必須 アカウント名50文字以下 W2 W7
        if 50 < len(customer_account):
            flash(errorMessages.w07('アカウント名', '50'))
            isValidateError = True
        if 0 >= len(customer_account):
            flash(errorMessages.w02('アカウント名'))
            isValidateError = True
        # 必須 パスワード6ｰ10文字 W2 W8
        if 6 >= len(customer_password) and 10 <= len(customer_password):
            flash(errorMessages.w08('パスワード', '6', '10'))
            isValidateError = True
        if 0 >= len(customer_password):
            flash(errorMessages.w02('パスワード'))
            isValidateError = True
        # 氏名20文字以下 W7
        if 20 <= len(customer_name):
            flash(errorMessages.w07('氏名', '20'))
            isValidateError = True
        # 郵便番号7文字 W6 W10
        if 7!= len(customer_zipcode):
            flash(errorMessages.w06('郵便番号', '7'))
            isValidateError = True
        if not customer_zipcode.isdigit():
            flash(errorMessages.w10('郵便番号'))
            isValidateError = True
        # 住所50文字以下 W7
        if 50 <= len(customer_address):
            flash(errorMessages.w07('住所', '50'))
            isValidateError = True
        # 電話番号10-11文字 W8 W10
        if 10 > len(customer_phone) or 11 < len(customer_phone):
            flash(errorMessages.w08('電話番号', '10', '11'))
            isValidateError = True
        if not customer_phone.isdigit():
            flash(errorMessages.w10('電話番号'))
            isValidateError = True

        # バリデーションフラグのチェック
        # 不備がある場合はアカウント情報変更画面にリダイレクト
        if isValidateError:
            return redirect(url_for('mypage_manage_account_edit'))

        # 会員IDの取得
        # customer_id = read_customer_one(session[logged_in_customer_id])
        customer = read_customer_one(1)
        customer_id=customer.customer_id

        # データベースを変更
        update_customer(customer_id, request)

        # 支払方法の表示設定
        if customer.customer_payment == "1":
            payment = "クレジットカード"
        elif customer.customer_payment == "2":
            payment = "PayPay"
        elif customer.customer_payment == "3":
            payment = "銀行振込"
        else:
            payment = "未選択"

        # アカウント情報画面に遷移
        return render_template("/customer/mypage/manage_account/info.html",
            customer_account = customer.customer_account,
            customer_password = customer.customer_password,
            customer_name = customer.customer_name,
            customer_zipcode = customer.customer_zipcode,
            customer_address = customer.customer_address,
            customer_phone = customer.customer_phone,
            customer_payment = payment)
    else:
        return redirect("/customer/auth/login")

# # 予約管理　list
# @app.route("/customer_manage_reservation", methods=["GET", "POST"])
# @is_customer_login
# def customer_manage_reservation():
#     # customer_id を取得
#     customer_id = session.get('logged_in_customer_id')
#     ticket_id = session.get('ticket_id')
#     event_id = session.get('event_id')

#     # customer_id を引数として渡す
#     tbl_reservation = read_reservation_customer_id(customer_id)
#     reservation_param_list = sorted(param_reservation(tbl_reservation),
#                                     key=itemgetter('event_date'))


#     # 予約情報が1件も取得できなければ、エラーメッセージ表示
#     if not reservation_param_list:
#         flash(errorMessages.w01('予約情報'))

#     return render_template("/customer/mypage/manage_ticket/list.html",
#                             reservation_param_list = reservation_param_list,
#                             event_id = event_id)
