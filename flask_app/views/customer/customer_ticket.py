from flask import render_template, redirect, url_for, request, flash, session
from flask_app.models.functions.event import read_event_one
from flask_app.models.functions.customer import read_customer_one
from flask_app.models.functions.ticket import convert_seat_id, read_ticket_one
from flask_app.models.functions.reservations import create_reservation
from flask_app.__init__ import app

@app.route("/ticket-reservation", methods=["POST", "GET"])
def create_new_reservation():
    event_id = request.args.get("event_id")
    ticket_id = request.form["ticket_id"]
    return redirect(
        url_for(
            "show_ticket_reservation_confirmation",
            event_id=event_id,
            ticket_id=ticket_id,
        )
    )

@app.route("/ticket-reservation/confirm")
def show_ticket_reservation_confirmation():
    event_id = request.args.get("event_id")
    ticket_id = request.args.get("ticket_id")

    event = read_event_one(event_id)
    ticket = read_ticket_one(ticket_id)
    ticket_seat = f"{convert_seat_id(ticket.ticket_seat_id)} (￥{ticket.ticket_price})"
    customer = read_customer_one(session["logged_in_customer_id"])
    payment=""
    if customer.customer_payment == "1":
        payment = "クレジットカード"
    elif customer.customer_payment == "2":
        payment = "PayPay"
    elif customer.customer_payment == "3":
        payment = "銀行振込"
    else:
        payment = "未選択"

    return render_template(
        "/customer/ticket/confirm_reservation.html",
        event=event,
        ticket=ticket,
        customer=customer,
        payment=payment,
        ticket_seat=ticket_seat
    )

@app.route("/ticket-reservation/confirm", methods=["POST"])
def submit_new_reservation():
    create_reservation(request)
    flash("チケットの予約に成功しました。")

    return redirect("/customer_top")
