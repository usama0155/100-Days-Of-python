MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_available(user_drink):
    for item in MENU[user_drink]["ingredients"]:
        if MENU[user_drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("Please insert coin: ")
    total = int(input("How many Quarters?: ")) *0.25
    total += int(input("How many dimes?: ")) *0.1
    total += int(input("How many nickels?: ")) *0.05
    total += int(input("How many pennies?: ")) *0.01
    return total
def is_transaction_successfull(money_received, coffee_cost):
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is ${change} change")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money Reunded")
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}") 

machine = True
while machine:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    if user_drink == 'off':
        machine = False
    elif user_drink == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_drink]
        if is_resource_available(user_drink):
            payment = process_coin()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(user_drink,drink["ingredients"])