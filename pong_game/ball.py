from turtle import Turtle

BALL_SPEED = 0.05

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALL_SPEED

    def move(self):
        new_ball_x = self.xcor() + self.x_move
        new_ball_y = self.ycor() + self.y_move
        self.goto(new_ball_x, new_ball_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.93

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = BALL_SPEED
        self.bounce_x()