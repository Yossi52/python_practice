from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0,9)

@app.route('/')
def home_path():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media0.giphy.com/media/LfbDxyQIWtzLTtMnc0/giphy.gif?cid=ecf05e47vdyfgndgk02r63btqv6pewrg0m0snr5cao9rc64e&rid=giphy.gif&ct=g' width=500px>"

@app.route('/<int:num>')
def guess_number(num):
    if int(num) > random_num:
        return f"<h1 style='color:purple'>{num} is too high, try again!</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif int(num) < random_num:
        return f"<h1 style='color:red'>{num} is too low, try again!</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif int(num) == random_num:
        return "<h1 style='color:blue'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
