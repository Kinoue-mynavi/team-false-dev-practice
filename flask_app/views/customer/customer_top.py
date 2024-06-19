from flask import render_template
from flask_app.__init__ import app

@app.route("/customer_top")
def customer_top():
    return render_template("/customer/customer_top.html")

