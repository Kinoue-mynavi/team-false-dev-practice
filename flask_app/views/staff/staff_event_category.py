from flask import render_template, flash, request, redirect, session, url_for
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.event import read_event
from flask_app.models.functions.event_category import create_event_category, delete_event_category, read_event_category, read_event_category_category_name, update_event_category
from flask_app.views.staff.common.staff_common import is_staff_login


# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()


# イベントカテゴリ管理 list
@app.route("/staff_manage_event_category", methods=["GET", "POST"])
@is_staff_login
def staff_manage_event_category():
    mst_event_category = read_event_category()
    mst_event = read_event()

    # イベントカテゴリーが1件も取得できなければ、エラーメッセージ表示
    if not mst_event_category:
        flash(errorMessages.w01('イベントカテゴリ'))

    # レコードの削除可否を判定
    # mst_event_categoryに直接値を追加できないので、新しい配列を作る
    mst_event_category_dict = []
    for event_category in mst_event_category:
        param = {'isDeletable': True,
                 'event_category_id': event_category.event_category_id,
                 'event_category_name': event_category.event_category_name
                 }

        for event in mst_event:
            # イベントカテゴリIDが一致するイベントカテゴリが存在していれば削除不可
            if event_category.event_category_id == event.event_category_id:
                param['isDeletable'] = False
        mst_event_category_dict.append(param)

    return render_template("/staff/manage_event_category/list.html", mst_event_category=mst_event_category_dict)


# イベントカテゴリ管理 input
@app.route("/staff_manage_event_category/<string:mode>/input", methods=["GET", "POST"])
@is_staff_login
def input_event_category(mode):
    formdata = session.get('event_category_formdata', None)

    if formdata:
        event_category_id = formdata['event_category_id']
        event_category_name = formdata['event_category_name']
        # session削除
        session.pop('event_category_formdata')
    else:
        if mode == "create":
            event_category_id = ''
            event_category_name = ''

        if mode == 'update':
            event_category_id = request.form['event_category_id']
            event_category_name = request.form['event_category_name']

    return render_template("/staff/manage_event_category/input.html", mode=mode, event_category_id=event_category_id, event_category_name=event_category_name)


# イベントカテゴリ管理 confirm
@app.route("/confirm_event_category/<string:mode>", methods=["POST"])
@is_staff_login
def confirm_event_category(mode):
    event_category_id = request.form['event_category_id']
    event_category_name = request.form['event_category_name']
    isValidateError = False

    # sessionに格納
    session['event_category_formdata'] = request.form

    # バリデーション
    if mode == 'create' or mode == 'update':
        if len(event_category_name) > 20:
            flash(errorMessages.w07('イベントカテゴリ名', '20'))
            isValidateError = True

    # イベントカテゴリ名の一意性チェック
    if mode == 'create':
        if read_event_category_category_name(event_category_name):
            flash(errorMessages.w03('イベントカテゴリ名'))
            isValidateError = True

    if isValidateError:
        # エラーがあれば入力画面に戻る
        # postにするためにcodeを指定する
        return redirect(url_for("input_event_category", mode=mode), code=307)
    else:
        # エラーがなければ確認画面に遷移
        return render_template("/staff/manage_event_category/confirm.html", event_category_id=event_category_id, event_category_name=event_category_name, mode=mode)


# イベントカテゴリ管理 accept
@app.route("/accept_event_category/<string:mode>", methods=["POST"])
@is_staff_login
def accept_event_category(mode):
    # session削除
    session.pop('event_category_formdata')

    event_category_id = request.form['event_category_id']
    if mode == 'create':
        create_event_category(request)
        flash(infoMessages.i01('イベントカテゴリ'))
    if mode == 'update':
        update_event_category(event_category_id, request)
        flash(infoMessages.i02('イベントカテゴリ'))
    if mode == 'delete':
        delete_event_category(event_category_id)
        flash(infoMessages.i03('イベントカテゴリ'))

    return redirect("/staff_manage_event_category")
