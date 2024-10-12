from turtle import Screen
from snake import Snake
from time import sleep

# initial screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)
screen.bgcolor("#252525")
screen.title("Snake Game")

# building the snake at the beginning
snake = Snake()

# Listening for key press to navigate the snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# games Main Loop
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()



screen.exitonclick()