PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    # print(names)


with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter.replace(PLACE_HOLDER, new_name)

        with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", "w") as letter_file:
                letter_file.write(new_letter)