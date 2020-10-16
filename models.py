from app import db


class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        """"""
        self.name = name

    def __repr__(self):
        return "<Brand: {}>".format(self.name)


class Price(db.Model):
    """"""
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    artist = db.relationship("Brand", backref=db.backref(
        "prices", order_by=id), lazy=True)


