# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
bid = True
while bid:

    username = input("Enter the bidders name: ")
    user_bid = int(input("Enter your bid: "))
    cont_bid = input("Continue bidding?\n(Y)es or (N). ").lower()
    auction_bids = {username: user_bid}
    if cont_bid == "no" or cont_bid == "n":
        bid = False




top_bid = {}
for key in auction_bids:
    for value in auction_bids[key]:
        if value > top_bid:
            top_bid = {key: value}

print(top_bid)