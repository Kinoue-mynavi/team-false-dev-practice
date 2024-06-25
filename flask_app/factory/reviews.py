# from flask_app.database import db
# from flask_app.models.mst_review import Mst_review
# from flask_app

# for i in range(3):
#     mst_review = Mst_review(
#         event_id = request.form["event_id"],
#         customer_id = request.form["customer_id"],
#         review_score = request.form["review_score"],
#         review_title = request.form["review_title"],
#         review_comment = request.form["review_comment"]
#     )
#     db.session.add(mst_review)
#     db.session.commit()

#     return