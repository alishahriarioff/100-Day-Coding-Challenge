from turtle import Turtle
UP    = 90
DOWN  = 270
LEFT  = 180
RIGHT = 0
class Snake:
    def __init__(self) -> None:
        self.speed      = 20
        self.snake_body = []
        self.x = 0
        self.y = 0
        self.create_snake()

    # Creates an snake with the lentgh of 3 in the beginning of the game
    def create_snake(self):
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("gray")
            segment.goto(x=self.x, y=self.y)
            self.x-=20
            self.snake_body.append(segment)

    # loops through the snake body in reverse and gives the x and y coordenates
    # of the front item to the current item
    # !!! Basicly Follows the Head Of snake every where it goes !!!
    def move(self):
        for segment_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)
        self.snake_body[0].forward(self.speed)

    # Navigating function that changes the heading (North/South/West/East) acurding to users response
    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)