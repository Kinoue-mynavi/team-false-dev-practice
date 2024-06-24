from flask_app.database import db
from flask_app.models.mst_event import Mst_event
from flask_app.models.mst_customer import Mst_customer


class Mst_review(db.Model):
    __tablename__ = "tbl_review"
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey(Mst_event.event_id))
    customer_id = db.Column(db.Integer, db.ForeignKey(Mst_customer.customer_id))
    review_score = db.Column(db.String(1))
    review_title = db.Column(db.String(30))
    review_comment = db.Column(db.String(500))

    def __init__(
        self,
        review_id=None,
        event_id=None,
        customer_id=None,
        review_score=None,
        review_title=None,
        review_comment=None
    ):
        self.review_id = review_id
        self.event_id = event_id
        self.customer_id = customer_id
        self.review_score = review_score
        self.review_title = review_title
        self.review_comment = review_comment

    def __repr__(self):
        return "<Tbl_reservation review_id:{} event_id:{} customer_id:{} review_score:{} review_title:{} review_comment:{}>".format(
            self.review_id,
            self.event_id,
            self.customer_id,
            self.review_score,
            self.review_title,
            self.review_comment
        )