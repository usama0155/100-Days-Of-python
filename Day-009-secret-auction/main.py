print("Welcome to secret auction program.")

def getting_data():
    name = input("What's your name: ")
    bid = int(input("What's your bid: $"))
    return name,bid

def getting_top_bidder(auction_db):
    max_bid = 0
    winner = ""
    for name in auction_db:
        bid = auction_db[name]
        if bid >= max_bid:
            max_bid = bid
            winner = name
    print(f"Winner is {winner} With highest bid of ${max_bid}")


def main():
    auction_db = {}

    while True:
        name , bid = getting_data()
        auction_db[name] = bid

        add_other = input("Are there other bidders? Type 'yes' OR 'no': ").lower()
        if add_other =='no':
            getting_top_bidder(auction_db)
            break
        else:
            print("\n"*30)

main()
