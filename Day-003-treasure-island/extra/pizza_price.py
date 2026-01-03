print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
cheese = input("Do you want extra cheese on your pizza? Y or N: ").lower()

if size == 's':
    total = 15
    if pepperoni == 'y' and size == 's':
        total += 2
        if cheese == 'y':
            total += 1
    print(f"Your final bill is: ${total}")
elif size == 'm':
    total = 20
    if pepperoni == 'y' and size != 's':
        total += 3
        if cheese == 'y':
            total += 1
        print(f"Your final bill is: ${total}")
elif size == 'l':
    total = 25
    if pepperoni == 'y':
        total += 3
        if cheese == 'y':
            total += 1
        print(f"Your final bill is: ${total}")
