# Higher or Lower Game

#TODO-1.import needed packages
from art import logo, vs
from data import data
from random import choice
from replit import clear


game_over = False
score = 0

#TODO: 2.write functions here
# getting a random choice from list
# comparing folowers count
def r_choice():
    c = choice(data)
    data.remove(c)
    return c

def compare(a, b):
    if a>b:
        return 'a'
    else:
        return 'b'

a = r_choice()
b = r_choice()
#TODO-3.main part of the code
while not game_over:
    print(logo)
    
    # print(a)
    # print(b)

    print(f"Score: {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Aginst B: {b['name']}, a {b['description']}, from {b['country']}.")
    answer = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
    cmpr = compare(a['follower_count'], b['follower_count'])
    if answer==cmpr:
        score+=1
        a = b
        b = r_choice()
        clear()
    else:
        game_over = True
        clear()
        print(f"You'r highest score: {score}")

