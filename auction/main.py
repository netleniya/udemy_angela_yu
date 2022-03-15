import os
from art import logo


def main():
    all_bids = {}
    auction = True

    print(logo)
    print("Welcome to the silent auction.")

    while auction:
        bidder_name = input("What is your name?: ").capitalize()
        try:
            bid_price = float(input("What's your bid?: £"))
            all_bids.update({bidder_name: bid_price})
        except ValueError:
            print("Value must be an integer")

        os.system('clear')

        more_bidders = input("Are there any other bidders? (Y/N): ").lower()

        if more_bidders.startswith("n"):
            auction = False

    try:
        winner = max(all_bids, key=all_bids.get)
        max_bid = max(all_bids.values())
        print(f"The winner is {winner} with a bid of £{max_bid:.2f}")
    except ValueError:
        print(f"There are no winners, just morons")


if __name__ == "__main__":
    main()
