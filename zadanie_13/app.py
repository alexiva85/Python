from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import zadanie_13.config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    from zadanie_13.models import GuestBookItem
    from zadanie_13.forms import GuestBookForm

    if request.method == 'POST':
        print(request.form)
        form = GuestBookForm(request.form)


        if form.validate():
            print(form.data)
            post = GuestBookItem(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = GuestBookItem.query.all()
    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    #for post in posts:
     #   print(post)

    return render_template('home.txt', posts=posts)

if __name__ == '__main__':
    from zadanie_13.models import *
    db.create_all()

    # Running app:
    app.run()