# Rock Paper Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print(f"{rock}    {paper}    {scissors}")
user_choice = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors. \n"))

if (user_choice==0) or (user_choice==1) or (user_choice==2):
    print("You'r move:\n"+game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("\nComputer's move:\n"+game_images[computer_choice])

    if (user_choice==0 and computer_choice==0) or (user_choice==1 and computer_choice==1) or (user_choice==2 and computer_choice==2):
        print("its a draw!")
    elif (user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
        print("congrats! You won! :)")
    else:
        print("Computer Win's! You lose! :(")   
else:
    print("invalid input! try again")
