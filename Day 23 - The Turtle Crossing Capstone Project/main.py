import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()



screen.listen()
screen.onkeypress(key="Up", fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_new_car()
    car.move_cars()

    # detects Collision between player and cars
    for c in car.cars:
        if player.distance(c) < 25:
            game_is_on = False
            screen.clear()
            score_board.game_over()
            

    # detect Collision between player and top of the screen
    if player.is_crossed_finish_line():
        player.reset_player()
        car.increace_car_speed()
        score_board.level_up()

screen.exitonclick()