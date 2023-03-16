from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)

response = requests.get("https://api.npoint.io/1f577d63e1339932abdc")
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Blog Question!\n\n"
                    f"Name: {name}\n"
                    f"email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}".encode("utf-8")
            )
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:post_id>')
def post_page(post_id):
    return render_template("post.html", all_posts=all_posts, ind=post_id-1)


if __name__ == "__main__":
    app.run(debug=True)
