from flask_app.__init__ import app
from flask import render_template, request
from flask_app.models.functions.event import read_event_one, is_expired_event
from flask_app.models.functions.event_category import read_event_category_one
from flask_app.models.functions.ticket import read_ticket_event_id, convert_seat_id
from flask_app.models.sessions.customer import has_auth_session
from flask_app.models.functions.review import calc_avarage_review_score, read_review_event_id, read_review_event_id_asc

@app.route("/event/<int:id>", methods=["POST", "GET"])
def show_event(id):
    event = read_event_one(id)

    # 「0：昇順」or「1：降順」
    query = "0" if not request.form else request.form['sorted_pattern']
    reviews = read_review_event_id_asc(id) if query == "0" else read_review_event_id(id)

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
        reviews=reviews,
        tickets=tickets,
        is_logged_in=has_auth_session(),
        is_expired=is_expired_event(event.event_date),
        avarage_review_score=calc_avarage_review_score(reviews),
        event_category_name=read_event_category_one(event.event_category_id).event_category_name
    )
