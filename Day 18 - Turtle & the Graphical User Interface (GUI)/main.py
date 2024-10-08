import turtle
import random
#----------------------------------------------------------------------------------extraxting color from an image using colorgram ->
# !!! NOTICE THAT !!! : -> This process only works in a Local Directory ! ---We Are in Clouds roght now :)---

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     R = color.rgb.r
#     G = color.rgb.g
#     B = color.rgb.b
#     new_color = (R, G, B)
#     rgb_colors.append(new_color)

# print(rgb_colors)

#----------------------------------------------------------------------------------------------------------------------------------

# rgb colors extracted using colorgram package: ->
rgb_colors = [
    (228, 236, 231),
    (194, 161, 114),
    (150, 78, 65),
    (136, 68, 80),
    (142, 168, 188),
    (189, 144, 160),
    (218, 202, 142),
    (52, 30, 46),
    (73, 88, 127),
    (196, 96, 77),
    (31, 29, 55),
    (177, 97, 116),
    (80, 123, 93),
    (131, 166, 144),
    (104, 43, 53),
    (61, 34, 28),
    (51, 52, 100),
    (110, 42, 38),
    (150, 150, 86),
    (219, 176, 186),
    (225, 177, 168),
    (96, 151, 117),
    (113, 119, 155),
    (86, 144, 157),
    (183, 185, 209),
    (161, 204, 209),
    (177, 201, 183)
    ]

t = turtle.Turtle()
t.hideturtle()
turtle.colormode(255)
t.penup()

def draw():
    x = -200
    y = -200
    for _ in range(10):
        for _ in range(10):
            t.teleport(x, y)
            t.dot(20, random.choice(rgb_colors))
            x += 50
        y += 50
        x = -200
        t.teleport(-200, y)

draw()

screen = turtle.Screen()
screen.exitonclick()
