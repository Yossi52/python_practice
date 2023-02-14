from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.bgcolor('grey80')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue' ,'navy', 'purple']


turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-120 + 40 * i)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.color()[0]
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if user_bet == winner_color:
    print(f"You win! The {winner_color} turtle is winner.")
else:
    print(f"You lose. The {winner_color} turtle is winner.")


screen.exitonclick()