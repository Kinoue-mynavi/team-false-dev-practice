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
