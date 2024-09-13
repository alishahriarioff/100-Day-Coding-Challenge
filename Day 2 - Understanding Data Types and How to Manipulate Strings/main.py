logo = """
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------                                                                                                                                                                                                                                
"""

print(logo)
total_bill = float(input("what was the total bill? \n"))
tip_percentage = int(input("what percentage tip would you like to give? 10, 12 or 15? \n"))
number_of_people = int(input("how many people to split the bill? \n"))

percentage = tip_percentage/100
tip_amount = total_bil*percentage
final_price = total_bil+tip_amount
resualt = round(final_price/number_of_people, 2)

print("Each person should pay: {:.2f}".format(resualt))