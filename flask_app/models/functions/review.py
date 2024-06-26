from flask_app.database import db
from flask_app.models.mst_review import Mst_review


# レビュー　新規登録
def create_review(request):
    mst_review = Mst_review(
        event_id = request.form["event_id"],
        customer_id = request.form["customer_id"],
        review_score = request.form["review_score"],
        review_title = request.form["review_title"],
        review_comment = request.form["review_comment"]
    )
    db.session.add(mst_review)
    db.session.commit()

    return

# レビュー　登録(スクリプトから実行用)
def create_review_script(param):
    mst_review = Mst_review(
        event_id = param["event_id"],
        customer_id = param["customer_id"],
        review_score = param["review_score"],
        review_title = param["review_title"],
        review_comment = param["review_comment"]
    )
    db.session.add(mst_review)
    db.session.commit()
    return


# レビュー　一覧取得
def read_review():
    mst_review = Mst_review.query.order_by(Mst_review.review_id.desc()).all()
    return mst_review

def read_review_asc():
    return Mst_review.query.all()


# レビュー　一件取得
def read_review_one(review_id):
    review = Mst_review.query.get(review_id)
    return review


# レビュー　会員IDを条件に取得
def read_review_customer_id(customer_id):
    review = Mst_review.query.filter(
        Mst_review.customer_id == customer_id).all()
    return review


# レビュー　イベントIDで取得
def read_review_event_id(event_id):
    review = Mst_review.query.filter(Mst_review.event_id == event_id).all()
    return review

# レビュー　イベントIDで取得
def read_review_event_id_asc(event_id):
    review = Mst_review.query.filter(Mst_review.event_id == event_id).order_by(Mst_review.review_id.desc()).all()
    return review


# レビュー　削除
def delete_review(review_id):
    review = Mst_review.query.get(review_id)

    db.session.delete(review)
    db.session.commit()

    return

# レビュースコアの平均を求める
def calc_avarage_review_score(reviews):
    if len(reviews) <= 0:
        return 0

    review_score_list = []
    for review in reviews:
        review_score_list.append(int(review.review_score))
    
    return round(sum(review_score_list) / len(review_score_list), 1)