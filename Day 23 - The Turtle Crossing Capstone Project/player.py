from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.create_player()

    def create_player(self):
        self.setheading(90)
        self.penup()
        self.reset_player()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def is_crossed_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
