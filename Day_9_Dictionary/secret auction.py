# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


auctions= {}
more_users = True
while more_users:
    new_name = input('Add new name: ')
    new_bid = int(input("Add your bid: € "))
    auctions[new_name] = new_bid
    answ = input("Want to add more users? (y/n): ")
    if answ != "y":
        more_users = False
    print("\n" * 100)
max_bid = 0
for key in auctions:
    if auctions[key] > max_bid:
        max_bid = auctions[key]

print(f"Oferta maxima: {max_bid}")