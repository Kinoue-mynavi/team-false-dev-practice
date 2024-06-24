from flask import render_template, request, flash
from flask_app.models.functions.event import read_event_one, is_expired_event
from flask_app.models.functions.event_category import read_event_category_one
from flask_app.models.functions.ticket import read_ticket_event_id, convert_seat_id
from flask_app.__init__ import app
from flask_app.messages import ErrorMessages, InfoMessages
from flask_app.models.sessions.customer import has_auth_session
from flask_app.models.functions.review import calc_avarage_review_score, read_review, read_review_asc

# エラーメッセージクラスのインスタンス作成
errorMessages = ErrorMessages()
# インフォメーションメッセージクラスのインスタンス作成
infoMessages = InfoMessages()

DUMMY_REVIEW_DATA = [
    {
        "review_id": 1,
        "customer_id": 1,
        "event_id": 1,
        "review_score": 3,
        "review_title": "レビューのタイトルが入ります",
        "review_comment": "これこれこういう理由であれこれ。そして、これこれこういう理由であれそれ",
    },
    {
        "review_id": 2,
        "customer_id": 2,
        "event_id": 2,
        "review_score": 4,
        "review_title": "レビューのタイトルが入ります",
        "review_comment": "これこれこういう理由であれこれ。そして、これこれこういう理由であれそれ",
    },
]

@app.route("/event/<int:id>", methods=["POST", "GET"])
def show_event(id):
    query = "0" if not request.form else request.form['sorted_pattern']
    mst_review = read_review_asc() if query == "0" else read_review()

    if not mst_review:
        flash(errorMessages.w01('レビュー'))
    
    event = read_event_one(id)
    event_category = read_event_category_one(event.event_category_id)
    is_expired = is_expired_event(event.event_date)
    reviews = DUMMY_REVIEW_DATA
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
        is_logged_in=has_auth_session(),
        is_expired=is_expired,
        event=event,
        reviews=reviews,
        tickets=tickets,
        avarage_review_score=calc_avarage_review_score(reviews),
        event_category_name=event_category.event_category_name
    )
