from flask import render_template, redirect, flash, url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.event import read_event
from flask_app.models.mst_event import Mst_event


# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

@app.route("/customer_top")
def customer_top():
    mst_events = read_event()
    # イベントが1件も取得できなければ、エラーメッセージ表示
    if not mst_events:
        flash(errorMessages.w01('イベントカテゴリ'))

    return render_template("/customer/customer_top.html", mst_events=mst_events)

