from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=self.x, y=self.y)
        

    def up(self):
        if self.ycor() < 245:
            new_y = self.ycor()+20
            self.goto(x=self.xcor(), y=new_y)
    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor()-20
            self.goto(x=self.xcor(), y=new_y)