from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the silent auction program. :)")
costumers = {}

def find_highest_bidder(bidders_dictionary):
    highest_bidder_name = ""
    highest_bid = 0

    for key in bidders_dictionary:
            if bidders_dictionary[key] > highest_bid:
                highest_bid = bidders_dictionary[key]
                highest_bidder_name = key
    print(f"the winner is {highest_bidder_name} with a bid of ${highest_bid}.")


auction_in_progress = True
while auction_in_progress:

    user_name = str(input("What is your name? "))
    bid_amount = int(input("What's your bid? $"))
    costumers[user_name] = bid_amount
    continue_to_bid = str(input("Are there any other bidders? type 'yes' or 'no' ")).lower()

    if continue_to_bid=="yes":
        clear()
    else:
        clear()
        auction_in_progress = False
        find_highest_bidder(costumers)

