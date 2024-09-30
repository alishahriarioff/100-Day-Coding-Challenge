from art import logo
import random

attempts = 0
number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game.")
print("Im thinking of a number between 1 and 100.")
dificulty = str(input("Choose a dificulty level, type 'easy' or 'hard': ")).lower()

if dificulty=="hard":
    attempts=5
elif dificulty=='easy':
    attempts=10
else:
    print("invalid input")

print(f"You have {attempts} to guess the number.")

while attempts!=0:
    guess = int(input("Make a geuwss: "))
    attempts-=1
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    elif guess == number:
        print("You win")
        print(f"with the {attempts}, of guesses remaining")
        break
    if attempts==0:
        print("You ran out of guesses you Lose!")
        break
    print("Guess again")
    print(f"you have {attempts} attempts remaning to guess.")