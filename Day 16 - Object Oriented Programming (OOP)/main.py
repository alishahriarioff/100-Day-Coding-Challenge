from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu_list = menu.get_items()[:-1]
is_on = True

print(logo)

while is_on:
    order = str(input(f"What would you like? ({menu_list}): ")).lower()

    if order=="report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    elif menu.find_drink(order_name=order):
        drink = menu.find_drink(order_name=order)
        if coffee_maker.is_resource_sufficient(drink=drink):
            if money_machine.make_payment(cost=drink.cost):  
                coffee_maker.make_coffee(order=drink)
    else:
        continue