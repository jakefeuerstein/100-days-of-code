from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book %r {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', book_list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form.get('title'), author=request.form.get('author'), rating=request.form.get('rating'))
        db.session.add(new_book)
        db.session.commit()
        # new_book = {
        #     'title': request.form['title'],
        #     'author': request.form.get('author'),
        #     'rating': request.form.get('rating')
        # }
        # all_books.append(new_book)
        # print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

