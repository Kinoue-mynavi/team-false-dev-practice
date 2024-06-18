from flask import render_template, flash, request, redirect, session, url_for
from flask_app.__init__ import app
from flask_app.views.staff.common.staff_common import is_staff_login
from flask_app.database import db
from flask_app.models.mst_customer import Mst_customer


# アカウント情報表示
@app.route("/customer_info", methods=["GET", "POST"])
@is_staff_login
def customer_info():
    # 表示するレコードを指定する
    # Mst_customer = session.query(Mst_customer).filter_by(customer_id = 1).first()

    customer_account = Mst_customer.customer_account
    customer_password = Mst_customer.customer_password
    customer_name = Mst_customer.customer_name
    customer_zipcode = Mst_customer.customer_zipcode
    customer_address = Mst_customer.customer_address
    customer_phone = Mst_customer.customer_phone
    customer_payment = Mst_customer.customer_payment

    return render_template("/customer/mypage/manage_accont/info.html",
                customer_account = customer_account,
                customer_password = customer_password,
                customer_name  =customer_name,
                customer_zipcode = customer_zipcode,
                customer_address = customer_address,
                customer_phone = customer_phone,
                customer_payment = customer_payment)