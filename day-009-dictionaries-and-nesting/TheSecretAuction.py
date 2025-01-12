import os

def new_bid(bidders: dict) -> bool:
    name = input("What is your name?\n")
    bid_amount = int(input("How much do you want to bid?\n$"))

    bidders[name] = bid_amount
    
    new_bidder = input("Is there another bidder? 'yes' or 'no'?\n")

    return new_bidder.lower() == "yes"


has_other_bidder = True 
bids = {"default": 0}

while has_other_bidder:
    has_other_bidder = new_bid(bids)
    os.system('cls||clear')

highest_bidder = "default"

for bidder, bid in bids.items():
    highest_bidder = bidder if bid > bids[highest_bidder] else highest_bidder

print(f"Highest bid is ${bids[highest_bidder]}. {highest_bidder} won!")