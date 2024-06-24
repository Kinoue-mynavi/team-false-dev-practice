from flask import render_template, redirect
from flask_app.models.functions.event import read_event_one
from flask_app.models.functions.event_category import read_event_category_one
from flask_app.models.functions.ticket import read_ticket_event_id, convert_seat_id, param_seat
from flask_app.__init__ import app

@app.route("/event/<int:id>", methods=["POST", "GET"])
def show_event(id):
    event = read_event_one(id)
    event_category = read_event_category_one(event.event_category_id)
    tickets = []
    for ticket in read_ticket_event_id(event.event_id):
        tickets.append({
            "ticket_id": ticket.ticket_id,
            "ticket_seat_id": ticket.ticket_seat_id,
            "ticket_seat_name": convert_seat_id(ticket.ticket_seat_id),
            "ticket_price": ticket.ticket_price
        })

    return render_template(
        "/customer/event/detail.html",
        event=event,
        tickets=tickets,
        event_category_name=event_category.event_category_name
    )