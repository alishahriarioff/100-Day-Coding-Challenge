from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "teal", "purple"]
turtels = []
race_on = False
x = -230
y = -150

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Witch Turtle Wins The Race? Choose a color.")

for i in range(7):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=x, y=y)
    turtels.append(t)
    y += 50

if user_bet in colors:
    race_on = True


while race_on:
    for t in turtels:
        if t.xcor() > 230:
            race_on = False
            winning_color = t.pencolor()
            if winning_color==user_bet:
                print(f"You won, {winning_color} is the winner!")
            else:
                print(f"You lost, {winning_color} is the winner!")
        rand = random.randint(0, 20)
        t.forward(rand)


screen.exitonclick()