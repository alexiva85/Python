from datetime import date

from zadanie_14.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(10), nullable=False) #, index=True

    # def __str__(self):
    #     return '<User_id %r, name %s>'.format(self.id, self.name)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False,  index=True)

    user = db.relationship(User, foreign_keys=[user_id, ])

    message = db.Column(db.String(50), unique=True, nullable=False)

    date_created = db.Column(db.Date, default=date.today)

    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post {}, user_id {}>'.format(self.id, self.user)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False, index=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    message = db.relationship(Message, foreign_keys=[message_id, ])

    user = db.relationship(User, foreign_keys=[user_id, ])

    comment = db.Column(db.String(50), unique=True, nullable=False) #если убрать юник, будет ошибка UNIQUE constraint failed: comment.comment почему???

    date_created = db.Column(db.Date, default=date.today)

    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    # def __str__(self):
    #     return '<Post %r, user_id %s>'.format(self.id, self.author)




    # def __str__(self):
    #     return '<Post %r, user_id %s>'.format(self.id, self.author)