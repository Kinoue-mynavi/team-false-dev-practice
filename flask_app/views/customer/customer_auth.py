
from flask import render_template, flash, request, redirect, session, url_for
from flask_app.__init__ import app
from flask import request
from flask_app.models.functions.customer import create_customer_script, read_customer_customer_account, delete_customer
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.sessions.customer import create_auth_session, has_auth_session

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

# 新規会員登録画面へ遷移
@app.route('/customer/auth/signup', methods=["GET"])
def new_member():
    return render_template("/customer/auth/signup.html")

# ログイン画面へ遷移
# デバック用
@app.route('/customer/auth/login', methods=["GET", "POST"])
def login():
    return render_template("/customer/auth/login.html")

# 新規会員登録 情報入力画面
@app.route('/customer/auth/signup', methods=['POST'])
def customer_new_member():
    # バリデーションフラグ
    isValidateError = False

    # フォームから送信されたデータを受け取る
    customer_account = request.form.get('customer_account')
    customer_password = request.form.get('customer_password')
    customer_name = request.form.get('customer_name')
    customer_zipcode = request.form.get('customer_zipcode')
    customer_address = request.form.get('customer_address')
    customer_phone = request.form.get('customer_phone')
    customer_payment = request.form.get('customer_payment')

    # バリデーションチェック
    # 必須 アカウント名50文字以下 W2 W7
    if 50 <= len(customer_account):
        flash(errorMessages.w07('アカウント名', '50'))
        isValidateError = True
    if 0 >= len(customer_account):
        flash(errorMessages.w02('アカウント名'))
        isValidateError = True
    # 必須 パスワード6ｰ10文字 W2 W8
    if 6 > len(customer_password) or 10 < len(customer_password):
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
    if 7!= len(customer_zipcode) or 0 != len(customer_zipcode):
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
    if 10 > len(customer_phone) or 11 < len(customer_phone) or 0 != len(customer_phone):
        flash(errorMessages.w08('電話番号', '10', '11'))
        isValidateError = True
    if not customer_phone.isdigit():
        flash(errorMessages.w10('電話番号'))
        isValidateError = True
    # アカウント名の一意性チェック W3
    if read_customer_customer_account(customer_account):
        flash(errorMessages.w03('アカウント名'))
        isValidateError = True

    # バリデーションフラグのチェック
    # 不備がある場合は新規会員登録にリダイレクト
    if isValidateError:
        return redirect(url_for('new_member'))

    # 入力情報を辞書型に入っているリスト型に入れる
    request_list = {"customer_account":customer_account, "customer_password":customer_password,
            "customer_name":customer_name, "customer_zipcode":customer_zipcode,
            "customer_address":customer_address, "customer_phone":customer_phone,
            "customer_payment":customer_payment}
    request_lists = [request_list]

    # データベースに追加
    create_customer_script(request_lists)

    # ログイン画面に遷移
    return render_template("customer/auth/login.html")


#会員ログアウト
@app.route("/customer/auth/logout", methods=["GET", "POST"])
def logout_customer():
    session.pop("logged_in_customer")
    session.pop("logged_in_customer_account")
    session.pop("logged_in_customer_id")
    session.pop("logged_in_customer_name")
    return redirect("/customer_top")


# 会員ログイン処理
@app.route("/customer/auth/login/login_customer", methods=["POST"])
def login_customer():
    isLoginError = False

    customer_account = request.form.get("customer_account")
    customer_password = request.form.get("customer_password")

    # アカウント名とパスワードが提供されているか確認
    if not customer_account or not customer_password:
        flash(errorMessages.w02('アカウント名またはパスワード'))
        return render_template("/customer/auth/login.html")

    customer_array = read_customer_customer_account(
        request.form["customer_account"])

    # 会員アカウントが存在するかチェック
    if not len(customer_array):
        flash(errorMessages.w04('アカウント名'))
        isLoginError = True
        return render_template("/customer/auth/login.html")

    # パスワードが一致するかチェック
    customer = customer_array[0]
    if request.form["customer_password"] != customer.customer_password:
        flash(errorMessages.w04('アカウント名'))
        isLoginError = True

    # エラーがあればログインページに遷移
    if isLoginError:
        return render_template("/customer/auth/login.html")

    else:
        # login処理を実行する
        create_auth_session()
        session["logged_in_customer_account"] = customer.customer_account
        session["logged_in_customer_id"] = customer.customer_id
        session["logged_in_customer_name"] = customer.customer_name
        flash(infoMessages.i05())
        return redirect("/customer_top")
    
# 会員退会処理
@app.route("/customer/mypage/manage_unsubscribe")
def confirm_unsubscribe():
    delete_customer(session["logged_in_customer_id"])
    session.pop("logged_in_customer")
    session.pop("logged_in_customer_account")
    session.pop("logged_in_customer_id")
    session.pop("logged_in_customer_name")
    return redirect("/customer_top")