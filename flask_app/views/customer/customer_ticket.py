from flask import render_template, redirect, url_for, request, flash
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
    # FIXME: sessionからcustomer_idを取得する
    customer = read_customer_one(1)

    return render_template(
        "/customer/ticket/confirm_reservation.html",
        event=event,
        ticket=ticket,
        customer=customer,
        ticket_seat=ticket_seat
    )

@app.route("/ticket-reservation/confirm", methods=["POST"])
def submit_new_reservation():
    create_reservation(request)
    flash("チケットの予約に成功しました。")

    return redirect("/customer_top")
