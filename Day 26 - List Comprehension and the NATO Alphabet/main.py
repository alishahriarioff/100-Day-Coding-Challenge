import pandas

nato_alhabet = pandas.read_csv(filepath_or_buffer="nato_phonetic_alphabet.csv")
# print(nato_alhabet)

nato_alhabet_dict = {row.letter:row.code for index,row in nato_alhabet.iterrows()}
# print(nato_alhabet_dict)


user_input = str(input("Enter a Word: ")).upper()

for char in user_input:
    if char in nato_alhabet_dict:
        print(f"{char}: {nato_alhabet_dict[char]}")

print()

nato_alphabet_name_list = [nato_alhabet_dict[item] for item in user_input]
print(nato_alphabet_name_list)