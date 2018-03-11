from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import zadanie_14.config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)

@app.route('/')
def index():

    posts = User.query.all()
    return render_template('home.txt', posts=posts)

@app.route('/users', methods=['GET', 'POST'])
def users():
    from zadanie_14.models import User
    from zadanie_14.forms import UserForm

    if request.method == 'POST':
        print(request.form)
        form = UserForm(request.form)

        if form.validate():
            user = UserForm(**form.data)
            db.session.add(user)
            db.session.commit()

            flash('User created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    users = User.query.all()

    return render_template('users.txt', users=users)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    from zadanie_14.models import Message
    from zadanie_14.forms import MessageForm

    if request.method == 'POST':
        print(request.form)
        form = MessageForm(request.form)
        print(form.data)

        if form.validate():
            message = Message(**form.data)
            db.session.add(message)
            db.session.commit()

            flash('Message created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    messages = Message.query.all()

    #posts = Post.query.all()
    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    for message in messages:
        # user_id = post.user_id
        # user = User.query.filter_by(id=user_id).first()
        print(message)



    return render_template('messages.txt', messages=messages)

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    from zadanie_14.models import Comment
    from zadanie_14.forms import CommentForm

    if request.method == 'POST':
        print(request.form)
        form = CommentForm(request.form)

        if form.validate():
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()

            flash('Comment created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    messages = Message.query.all()
    comments = Comment.query.all()

    # for com in comments:
    #     print (com.message.message, com.user.name, com.message.date_created)

    return render_template('comments.txt', comments=comments, messages = messages)

def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(name='Ivan')

    db.session.add(ivan)
    db.session.commit()  # note

if __name__ == '__main__':
    from zadanie_14.models import *
    db.create_all()

    if User.query.count() == 0:
        populate_db()

    # Running app:
    app.run()