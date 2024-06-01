import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #detect the turtle collides with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on= False
            scoreboard.game_over()

    #detect the player reach to other side
    if player.is_at_finish_line():
        player.go_to_stat()
        car_manager.level_up()
        scoreboard.increase_score()





screen.exitonclick()
