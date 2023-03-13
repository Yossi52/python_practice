from flask import Flask, render_template
from post import Post


app = Flask(__name__)

all_post = Post()

@app.route('/')
def home():
    blog_data = all_post.blog_data
    return render_template("index.html", data=blog_data)

@app.route('/post/<int:num>')
def get_post(num):
    blog = all_post.blog_data[int(num)-1]
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
