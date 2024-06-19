from flask import render_template
from flask_app.__init__ import app
from flask_app.views.staff.common.staff_common import is_staff_login
from flask_app.models.functions.customer import read_customer_one


# アカウント情報表示
@app.route("/customer_info", methods=["GET", "POST"])
@is_staff_login
def customer_info():
    # 表示するレコードを指定する
    # customer = read_customer_one(session[logged_in_customer_id])
    customer = read_customer_one(1)

    if customer.customer_payment == "1":
        payment = "クレジットカード"
    
    elif customer.customer_payment == "2":
        payment = "PayPay"
    
    elif customer.customer_payment == "3":
        payment = "銀行振込"
    
    else:
        payment = "未選択"


    return render_template("/customer/mypage/manage_accont/info.html",
                customer_account = customer.customer_account,
                customer_password = customer.customer_password,
                customer_name = customer.customer_name,
                customer_zipcode = customer.customer_zipcode,
                customer_address = customer.customer_address,
                customer_phone = customer.customer_phone,
                customer_payment = payment)