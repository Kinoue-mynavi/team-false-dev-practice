from flask import render_template, flash, request, redirect, session, url_for, Markup
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.functions.event import create_event, delete_event, read_event, read_event_event_category, read_event_event_name, update_event
from flask_app.models.functions.event_category import event_category_name_judge, read_event_category
from flask_app.models.functions.ticket import read_ticket
from flask_app.views.staff.common.staff_common import is_staff_login


# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()


# イベント管理 list
@app.route("/staff_manage_event", methods=["GET", "POST"])
@is_staff_login
def staff_manage_event():
    mst_event_category = read_event_category()
    mst_ticket = read_ticket()

    # セレクトボックスでの絞り込み
    if not request.form:
        query = "0"
    else:
        query = request.form['event_category_id']

    if query == "0":
        mst_event = read_event()
    else:
        mst_event = read_event_event_category(query)

    # イベントが1件も取得できなければ、エラーメッセージ表示
    if not mst_event:
        flash(errorMessages.w01('イベント'))

    # セレクトボックスを動的生成
    selectbox_option = ''
    for event_category in mst_event_category:
        if query != 0 and str(query) == str(event_category.event_category_id):
            selectbox_option += '<option value=' + str(event_category.event_category_id) + \
                ' selected>' + event_category.event_category_name + '</option>'
        else:
            selectbox_option += '<option value="' + str(event_category.event_category_id) + \
                '">' + event_category.event_category_name + '</option>'

    # レコードの削除可否を判定
    # mst_eventに直接値を追加できないので、新しい配列を作る
    mst_event_dict = []
    for event in mst_event:
        param = {'isDeletable': True,
                 'event_id': event.event_id,
                 'event_category_id': event.event_category_id,
                 'event_name': event.event_name,
                 'event_date': event.event_date,
                 'event_place': event.event_place,
                 'event_overview': event.event_overview
                 }
        for ticket in mst_ticket:
            if event.event_id == ticket.event_id:
                param['isDeletable'] = False
        mst_event_dict.append(param)

    return render_template("/staff/manage_event/list.html", mst_event=mst_event_dict, mst_event_category=mst_event_category, selectbox_option=Markup(selectbox_option))


# イベント管理 input
@app.route("/staff_manage_event/<string:mode>/input", methods=["GET", "POST"])
@is_staff_login
def input_event(mode):
    mst_event_category = read_event_category()
    formdata = session.get('event_formdata', None)

    if formdata:
        event_id = formdata['event_id']
        event_name = formdata['event_name']
        event_category_id = formdata['event_category_id']
        event_date = formdata['event_date']
        event_place = formdata['event_place']
        event_overview = formdata['event_overview']
        # session削除
        session.pop('event_formdata')
    else:
        if mode == 'create':
            event_id = '',
            event_name = ''
            event_category_id = ''
            event_date = ''
            event_place = ''
            event_overview = ''

        if mode == 'update':
            event_id = request.form['event_id']
            event_name = request.form['event_name']
            event_category_id = request.form['event_category_id']
            event_date = request.form['event_date']
            event_place = request.form['event_place']
            event_overview = request.form['event_overview']
    # セレクトボックスを動的生成
    selectbox_option = ''
    for event_category in mst_event_category:
        if str(event_category_id) == str(event_category.event_category_id):
            selectbox_option += '<option value=' + str(event_category.event_category_id) + \
                ' selected>' + event_category.event_category_name + '</option>'
        else:
            selectbox_option += '<option value="' + str(event_category.event_category_id) + \
                '">' + event_category.event_category_name + '</option>'

    return render_template("/staff/manage_event/input.html",
                           mst_event_category=mst_event_category,
                           event_id=event_id,
                           event_name=event_name,
                           event_category_id=event_category_id,
                           event_date=event_date,
                           event_place=event_place,
                           event_overview=event_overview,
                           mode=mode,
                           selectbox_option=Markup(selectbox_option))


# イベント管理 confirm
@app.route("/confirm_event/<string:mode>", methods=["POST"])
@is_staff_login
def confirm_event(mode):
    mst_event_category = read_event_category()

    event_id = request.form['event_id']
    event_name = request.form['event_name']
    event_category_id = request.form['event_category_id']
    event_date = request.form['event_date']
    event_place = request.form['event_place']
    event_overview = request.form['event_overview']
    isValidateError = False
    # sessionに格納
    session['event_formdata'] = request.form

    # バリデーション
    if mode == 'create' or mode == 'update':
        if len(event_name) > 50:
            flash(errorMessages.w07('イベント名', '50'))
            isValidateError = True

        if len(event_place) > 30:
            flash(errorMessages.w07('開催場所', '30'))
            isValidateError = True

        if len(event_overview) > 200:
            flash(errorMessages.w07('イベント概要', '200'))
            isValidateError = True

    # イベント名の一意性チェック
    if mode == 'create':
        if read_event_event_name(event_name):
            flash(errorMessages.w03('イベント名'))
            isValidateError = True

    if isValidateError:
        # エラーがあれば入力画面に戻る
        # postにするためにcodeを指定する
        return redirect(url_for("input_event", mode=mode), code=307)

    else:
        # エラーがなければ確認画面に遷移
        return render_template("/staff/manage_event/confirm.html",
                               event_id=event_id,
                               event_name=event_name,
                               event_category_id=event_category_id,
                               event_category_name=event_category_name_judge(
                                   mst_event_category, event_category_id),
                               event_date=event_date,
                               event_place=event_place,
                               event_overview=event_overview,
                               mode=mode)


# イベント管理 accept
@app.route("/accept_event/<string:mode>", methods=["POST"])
@is_staff_login
def accept_event(mode):
    # session削除
    session.pop('event_formdata')

    event_id = request.form['event_id']
    if mode == 'create':
        create_event(request)
        flash(infoMessages.i01('イベント'))
    if mode == 'update':
        update_event(event_id, request)
        flash(infoMessages.i02('イベント'))
    if mode == 'delete':
        delete_event(event_id)
        flash(infoMessages.i03('イベント'))

    return redirect("/staff_manage_event")
