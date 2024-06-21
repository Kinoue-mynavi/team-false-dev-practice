from flask import render_template
from flask_app.models.functions.event import read_event_one
from flask_app.models.functions.event_category import read_event_category_one
from flask_app.__init__ import app

@app.route("/event/<int:id>")
def show_event(id):
    event = read_event_one(id)
    event_category = read_event_category_one(event.event_category_id)
    return render_template("/customer/event/detail.html", event=event, event_category_name=event_category.event_category_name)
