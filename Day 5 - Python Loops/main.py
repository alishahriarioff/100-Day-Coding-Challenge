#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

logo = """                                                                                            
                      ██████████                                                            
                  ████░░░░░░░░░░██████                    ░░                                
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
            ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░████████████████████████████████            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
          ██░░░░██      ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▓▓░░░░░░░░██            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░██████░░██  ██░░░░██  ████████              
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██    ██      ████                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
                  ████░░░░░░░░░░██████                                                      
                  ░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░                                                      
                                                                                            """
print(logo)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

                    #Eazy Level - Order not randomised:
                    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"........................................................................................"
# My easy soluation: ->

# letter = []
# for i in range(1, nr_letters+1):
#     random_num = random.randint(0, len(letters)-1)
#     letter.append(letters[random_num])

# symbol = []
# for i in range(1, nr_symbols+1):
#     random_num = random.randint(0, len(symbols)-1)
#     symbol.append(symbols[random_num])

# number = []
# for i in range(1, nr_numbers+1):
#     random_num = random.randint(0, len(numbers)-1)
#     number.append(numbers[random_num])

# letter = "".join(letter)
# symbol = "".join(symbol)
# number = "".join(number)
# print("The easy soluation is: ")
# print(letter+symbol+number)
"........................................................................................"
"........................................................................................"
# Angella's easy soluation: ->
password = ""
for i in range(1, nr_letters+1):
    password += random.choice(letters)

symbol = []
for i in range(1, nr_symbols+1):
    password += random.choice(symbols)

number = []
for i in range(1, nr_numbers+1):
    password += random.choice(numbers)

print(password)
"........................................................................................"
                    #Hard Level - Order of characters randomised:
                    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"........................................................................................"
# My hard soluation: ->

# letter = []
# for i in range(1, nr_letters+1):
#     random_num = random.randint(0, len(letters)-1)
#     letter.append(letters[random_num])

# symbol = []
# for i in range(1, nr_symbols+1):
#     random_num = random.randint(0, len(symbols)-1)
#     symbol.append(symbols[random_num])

# number = []
# for i in range(1, nr_numbers+1):
#     random_num = random.randint(0, len(numbers)-1)
#     number.append(numbers[random_num])

# letter = "".join(letter)
# symbol = "".join(symbol)
# number = "".join(number)
# new_combo = letter+symbol+number
# print(new_combo)
# new_combo_list = []
# for i in range(0, len(new_combo)):
#     new_combo_list.append(new_combo[i])
# print(new_combo_list)


# hard_answer = []
# for i in range(1, len(new_combo_list)+1):
#     random_num = random.randint(0, len(new_combo_list)-1)
#     hard_answer.append(new_combo_list[random_num])
#     del new_combo_list[random_num]


# print(hard_answer)
# print("".join(hard_answer))
"........................................................................................"
"........................................................................................"
# Angella's hard soluation: ->
password_list = []
for i in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

symbol = []
for i in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

number = []
for i in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
print("".join(password_list))

"........................................................................................"