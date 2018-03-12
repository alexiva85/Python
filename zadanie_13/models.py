from datetime import date

from zadanie_13.app import db



class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    author = db.Column(db.String, nullable=False, index=True)

    message = db.Column(db.String(5), unique=True, nullable=False)

    date_created = db.Column(db.Date, default=date.today)

    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r, user_id %s>'.format(self.id, self.author)