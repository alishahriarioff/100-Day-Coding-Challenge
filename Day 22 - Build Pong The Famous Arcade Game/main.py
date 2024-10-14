from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# initial screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("#252525")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()
score_board = ScoreBoard()


screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)

    ball.move()

    # check collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # check collision with right and left paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # check collision with the right wall and gives left a point
    if ball.xcor() > 380:
        ball.reset_ball()
        score_board.l_point()
    
    # check collision with the left wall and gives right a point
    if ball.xcor() < -380:
        ball.reset_ball()
        score_board.r_point()




screen.exitonclick()