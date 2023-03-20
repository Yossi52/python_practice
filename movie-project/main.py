import sqlalchemy.exc
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap(app)

# DB 생성 / 연결
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 영화 정보 API endpoint
MOVIE_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAIL_ENDPOINT = "https://api.themoviedb.org/3/movie/"
MOVIE_KEY = os.getenv("MOVIE_API_KEY")


# movie 테이블 생성
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(500), nullable=False)


# 영화 리뷰와 평정 업데이트 폼
class UpdateRating(FlaskForm):
    new_rating = DecimalField("Your Rating Out Of 10 e.g. 6.8", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


# 영화 찾기 위한 제목을 입력하는 폼
class FindMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# 홈페이지 렌더링
@app.route("/")
def home():
    with app.app_context():
        try:
            # 영화 평점 순으로 정렬
            all_movies = Movie.query.order_by(Movie.rating).all()
        except sqlalchemy.exc.OperationalError:
            all_movies = []
    # 영화 평점 순으로 랭킹 부여
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    return render_template("index.html", movies=all_movies)


# 평점과 리뷰 수정하는 페이지
@app.route('/edit/id/<movie_id>', methods=["GET", "POST"])
def edit(movie_id):
    form = UpdateRating()
    with app.app_context():
        movie_to_edit = Movie.query.get(movie_id)
        if request.method == "POST" and form.validate_on_submit():
            movie_to_edit.rating = form.data.get("new_rating")
            movie_to_edit.review = form.data.get("new_review")
            db.session.commit()
            return redirect(url_for("home"))

        return render_template("edit.html", movie=movie_to_edit, form=form)


# 영화 삭제하는 페이지 (따로 페이지가 렌더링 되지는 않음)
@app.route('/delete/id/<movie_id>')
def delete(movie_id):
    with app.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for("home"))


# 제목으로 영화를 추가할 수 있는 페이지
@app.route('/add', methods=["GET", "POST"])
def add():
    form = FindMovie()
    if request.method == "POST" and form.validate_on_submit():
        find_title = form.data.get("title")
        header = {
            "api_key": MOVIE_KEY,
            "query": find_title,
            "include_adult": "True"
        }
        response = requests.get(MOVIE_SEARCH_ENDPOINT, params=header)
        response.raise_for_status()
        movie_list = response.json()["results"]
        return render_template("select.html", list=movie_list)

    return render_template("add.html", form=form)


# select.html에 표시될 여러 영화 제목 중에 하나를 선택하면 DB에 저장
@app.route('/add_to_db/<movie_api_id>')
def add_to_db(movie_api_id):
    response = requests.get(f"{MOVIE_DETAIL_ENDPOINT}{movie_api_id}", params={"api_key": MOVIE_KEY})
    response.raise_for_status()
    movie_info = response.json()
    with app.app_context():
        new_movie = Movie(
            id=movie_info["id"],
            title=movie_info["title"],
            year=movie_info["release_date"][:4],
            description=movie_info["overview"],
            img_url=f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{movie_info['poster_path']}"
        )
        db.create_all()
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for("edit", movie_id=movie_api_id))


if __name__ == '__main__':
    app.run(debug=True)
