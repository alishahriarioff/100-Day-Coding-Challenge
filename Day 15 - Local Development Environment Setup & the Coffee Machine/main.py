from art import logo
from data import MENU, resources


print(logo)
print("The Coffee Mechine Simulator.")

menu   = list(MENU.keys())
water  = resources["water"]
milk   = resources["milk"]
coffee = resources["coffee"]
money  = 0
coffee_mechine_working = True


def report():
    print(f"water: {water}ml")
    print(f"milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"money: ${money}")
def check_res(order):
    if order=="espresso":
        if (water > MENU[order]["ingredients"]["water"]) and (coffee > MENU[order]["ingredients"]["coffee"]):
            return True
        else:
            return False
    elif (water > MENU[order]["ingredients"]["water"]) and (milk > MENU[order]["ingredients"]["milk"]) and (coffee > MENU[order]["ingredients"]["coffee"]):
        return True
    else:
        return False
def get_money():
    QUARTER = 0.25
    DIME    = 0.10
    NICKLE  = 0.05
    PENNY   = 0.01
    quarters = float(input("\thow many quarters?: "))
    dimes = float(input("\thow many dimes?: "))
    nickles = float(input("\thow many nickles?: "))
    pennies = float(input("\thow many pennies?: "))
    money = (quarters*QUARTER) + (dimes*DIME) + (nickles*NICKLE) + (pennies*PENNY)
    return money

while coffee_mechine_working:
    order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    if order=="report":
        report()
    elif order in menu:
        if check_res(order):
            payment = get_money()
            if payment>=MENU[order]["cost"]:
                money+=MENU[order]["cost"]
                water-=MENU[order]["ingredients"]["water"]
                if order=="coffee":
                    milk-=MENU[order]["ingredients"]["milk"]
                coffee-=MENU[order]["ingredients"]["coffee"]
                change = payment-MENU[order]["cost"]
                print(f"\nHere is you'r change: ${round(change, 2)}")
                print(f"Here is you'r {order} ☕️. Enjoy!\n")
            else:
                print(f"You dont have enough money.\nHere is you'r money back ${payment}")
            
        else:
            print("There is not enough resources...sorry!")
            coffee_mechine_working = False
    else:
        print("This Ithem Is Not Availible, Try Again!")
        coffee_mechine_working = False