from flask import render_template
from flask_app.__init__ import app

@app.route("/customer_top")
def customer_top():
    return render_template("/customer/mypage/manage_accont/info.html")

# /customer/customer_top.html