from flask import render_template
from flask_app.__init__ import app
from flask import Flask, request
from flask_app.models.functions.customer import create_customer_script

# app = Flask(__name__)

# 新規会員登録画面へ遷移
@app.route('/new_member', methods=["GET", "POST"])
def new_member():
    return render_template("/customer/auth/signup.html")

# ログイン画面へ遷移
@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("/customer/auth/login.html")

# 新規会員登録 情報入力画面
@app.route('/customer_new_member', methods=['POST'])
def customer_new_member():
    # フォームから送信されたデータを受け取る
    # デバック用
    customer_account = request.form.get('customer_account')
    customer_password = request.form.get('customer_password')
    customer_name = request.form.get('customer_name')
    customer_zipcode = request.form.get('customer_zipcode')
    customer_address = request.form.get('customer_address')
    customer_phone = request.form.get('customer_phone')
    customer_payment = request.form.get('customer_payment')

    request_list = {"customer_account":customer_account, "customer_password":customer_password,
            "customer_name":customer_name, "customer_zipcode":customer_zipcode,
            "customer_address":customer_address, "customer_phone":customer_phone,
            "customer_payment":customer_payment}
    request_lists = [request_list]

    # データベースに追加
    create_customer_script(request_lists)

    # ログイン画面に遷移
    return render_template("customer/auth/login.html")