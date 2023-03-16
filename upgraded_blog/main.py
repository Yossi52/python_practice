from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/1f577d63e1339932abdc")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<int:post_id>')
def post_page(post_id):
    return render_template("post.html", all_posts=all_posts, ind=post_id-1)


if __name__ == "__main__":
    app.run(debug=True)
