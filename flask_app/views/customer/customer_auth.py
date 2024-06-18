from flask import render_template
from flask_app.__init__ import app
from flask import Flask, request

# app = Flask(__name__)

@app.route('/new_member', methods=["GET", "POST"])
def new_member():
    return render_template("/customer/auth/signup.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("/customer/auth/login.html")



@app.route('/login', methods=['POST'])
def customer_new_member():
    # フォームから送信されたデータを受け取る
    customer_account = request.form.get('customer_account')
    customer_password = request.form.get('customer_password')
    customer_name = request.form.get('customer_name')
    customer_zipcode = request.form.get('customer_zipcode')
    customer_address = request.form.get('customer_address')
    customer_phone = request.form.get('customer_phone')
    customer_payment = request.form.get('customer_payment')

    print(customer_account)

    # return render_template("customer/auth/login.html")