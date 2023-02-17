import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    if car_manager.collision_with_player(player):
        game_is_on = False
        scoreboard.game_over()

    if player.is_finish_line():
        player.reset_position()
        car_manager.speed_up()
        scoreboard.increase_level()
        scoreboard.update_level()

screen.exitonclick()
