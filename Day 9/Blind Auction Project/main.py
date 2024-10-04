import os



# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def top_bid(list_of_bids):
    winner = ""
    winning_bid = 0
    for bidder in list_of_bids:
        bid_amount = list_of_bids[bidder]
        if  winning_bid < bid_amount:
            winner = bidder
            winning_bid = bid_amount
    print(f"{winner} won with a bid of {winning_bid}")

cont_bid = True
auction_bids = {}
while cont_bid:
    name = input("Enter the bidders name: ")
    amount = int(input("Enter your bid: "))
    auction_bids[name] = amount
    cont_to_bid = input("Continue bidding?\n(Y)es or (N). ").lower()

    if cont_to_bid == "no" or cont_to_bid == "n":
        cont_bid = False
        top_bid(auction_bids)
    elif cont_to_bid == "yes" or cont_to_bid =="y":
        print("\n" * 10)