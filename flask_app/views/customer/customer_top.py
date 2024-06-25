from flask import render_template, redirect, flash, url_for, request
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.event import read_event
from flask_paginate import Pagination, get_page_parameter

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

@app.route("/customer_top")
def customer_top():
    # 一覧のレコードを取得
    mst_events = read_event()
    displayed_events = []
    # イベントが1件も取得できなければ、エラーメッセージ表示
    if not mst_events:
        flash(errorMessages.w01('イベントカテゴリ'))
    else:
        # ページネーション
        ## 現在のページ番号を取得
        page = int(request.args.get(get_page_parameter(), 1))
        ## ページごとの表示件数
        per_page = 10
        ## ページネーションオブジェクトを作成
        pagination = Pagination(page=page, per_page=per_page, total=len(mst_events))
        # 表示するデータを取得
        start = (page - 1) * per_page
        end = start + per_page
        displayed_events = mst_events[start:end]


    return render_template("/customer/customer_top.html", mst_events=displayed_events, pagination=pagination)
