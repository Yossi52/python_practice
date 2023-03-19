import sqlalchemy.exc
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return {"title": self.title, "author": self.author, "rating":self.rating}


@app.route('/')
def home():
    with app.app_context():
        try:
            all_books = db.session.query(Book).all()
        except sqlalchemy.exc.OperationalError:
            all_books = []

    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_data = request.form
        with app.app_context():
            db.create_all()
            new_book = Book(title=book_data["title"], author=book_data["author"], rating=float(book_data["rating"]))
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route('/edit/id/<book_id>', methods=["GET", "POST"])
def edit_rating(book_id):
    with app.app_context():
        book_to_update = Book.query.get(book_id)
        if request.method == "POST":
            book_to_update.rating = request.form["new_rating"]
            db.session.commit()
            return redirect(url_for("home"))

        return render_template("edit.html", book=book_to_update)


@app.route('/delete/id/<book_id>')
def book_delete(book_id):
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

