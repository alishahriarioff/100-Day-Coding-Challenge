from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y_pos = randint(-250, 250)
            new_car.goto(x=300, y=random_y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increace_car_speed(self):
        self.car_speed += MOVE_INCREMENT