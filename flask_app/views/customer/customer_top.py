from flask import render_template
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions. import


# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

@app.route("/customer_top")
def customer_top():

    # イベントカテゴリーが1件も取得できなければ、エラーメッセージ表示
    if not mst_customer:
        flash(errorMessages.w01('イベントカテゴリ'))

    return render_template("/customer/customer_top.html")