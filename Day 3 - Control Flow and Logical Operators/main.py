print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = str(input("You'r at a cross road, where do you want to go? type \"Left\" or \"Right\" ")).lower()
if choice1 == "left":
    choice2 = str(input("You come to a lake, there is an island in the middle of the lake, type \"wait\" to wait for a boat or \"swim\" to swom across? ")).lower()
    if choice2 == "wait":
        choice3 = str(input("You arrived at the island unharmed, There is a house with 3 doors, one \"red\", one \"yellow\" and one \"blue\" wich color do you choose? ")).lower()
        if choice3 == "yellow":
            print("Congrats, You Win!")
        else:
            if choice3 == "red":
                print("behind this door was a dragon, he attacked you and killed you, Game Over!")
            else:
              print("behind this door was a hellhound he draged your soul to hell, Game Over!")  
    else:
        print("pirana fish attacked you and ate you, Game Over!")
else:
    print("you fell into a hole, Game Over!")