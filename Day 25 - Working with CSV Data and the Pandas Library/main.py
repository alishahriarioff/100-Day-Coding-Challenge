import turtle
import pandas

states_guessed_count = 0
states_guessed_list = []
game_is_on = True

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle(visible=False)
t.penup()

data = pandas.read_csv(filepath_or_buffer="50_states.csv")
states = data.state.to_list()

while game_is_on:
    missed_state = []
    if len(states_guessed_list) == 50:
        game_is_on = False

    guess = screen.textinput(title=f"{states_guessed_count}/50 State you guessed.", prompt="Can You Guess the Name of States?")
    guess = guess.title()
    
    if guess == "Exit":
        missed_state = []
        for state in states:
            if state not in states_guessed_list:
                missed_state.append(state)
        df = pandas.DataFrame(missed_state)
        df.to_csv(path_or_buf="missed-states.csv")
        break

    if (guess in states) and (guess not in states_guessed_list):
        print(True)
        states_guessed_count += 1
        states_guessed_list.append(guess)

        s = data[data.state == guess]
        print(s)
        x = int(s['x'])
        y = int(s['y'])

        t.goto(x=x, y=y)
        t.write(guess, False, "left", ("Arial", 8, "bold"))