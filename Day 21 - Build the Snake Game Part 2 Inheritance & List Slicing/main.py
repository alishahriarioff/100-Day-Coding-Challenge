from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from time import sleep

# initial screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)
screen.bgcolor("#252525")
screen.title("Snake Game")

scoreboard = ScoreBoard()

# building the snake at the beginning
snake = Snake()

# Creating the food
food = Food()



# Listining for key press to navigate the snake
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

    # checks the collision between snake head and food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        scoreboard.increce_score()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        screen.listen()

    for body in snake.snake_body[1:]:
        if snake.snake_body[0].distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()