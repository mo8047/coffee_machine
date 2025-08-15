MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins(u_order):

    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01

    u_quarters = int(input("How many quarters: "))
    u_quarters *= quarters

    u_dimes = int(input("How many dimes: "))
    u_dimes *= dimes

    u_nickels = int(input("How many nickels: "))
    u_nickels *= nickels

    u_pennies = int(input("How many pennies: "))
    u_pennies *= pennies

    total_amount = u_quarters + u_dimes + u_nickels + u_pennies
    print(total_amount)

    espresso_amount = MENU["espresso"]["cost"]
    latte_amount = MENU["latte"]["cost"]
    cappuccino_amount = MENU["cappuccino"]["cost"]

    if u_order == "cappuccino":
        print(f"Cappuccino price is {cappuccino_amount}")
        if total_amount > cappuccino_amount:
            return_user = total_amount - cappuccino_amount
            print(f"Here's your change {return_user}")
            print("Enjoy, Come back!")
        elif cappuccino_amount > total_amount:
            print(f"You're short {cappuccino_amount - total_amount}")
        else:
            print("Enjoy, Come back!")
    elif u_order == "latte":
        print(f"latte price is {latte_amount}")
        if total_amount > latte_amount:
            return_user = total_amount - latte_amount
            print(f"Here's your change {return_user}")
            print("Enjoy, Come back!")
        elif latte_amount > total_amount:
            print(f"You're short {latte_amount - total_amount}")
        else:
            print("Enjoy, Come back!")

    elif u_order == "espresso":
        print(f"espresso price is {espresso_amount}")
        if total_amount > espresso_amount:
            return_user = total_amount - espresso_amount
            print(f"Here's your change {return_user}")
            print("Enjoy, Come back!")
        elif espresso_amount > total_amount:
            print(f"You're short {espresso_amount - total_amount}")
        else:
            print("Enjoy, Come back!")




def order():
    u_order = input("What would you like?(Cappuccino, latte, espresso): ").lower()
    if u_order == "report":
        print(resources)
    elif u_order in ["cappuccino", "latte", "espresso"]:
        resource_requirement(u_order)
    else:
        print("Invalid Input")
        exit()

def resource_requirement(u_order):
    if u_order == "cappuccino" and resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
        coins(u_order)
    elif u_order == "latte" and resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
        coins(u_order)
    elif u_order == "espresso" and resources["water"] >= 50 and resources["coffee"] >= 18:
        coins(u_order)
    else:
        print("Unavailable resources. Come back later.")

while True:
    order()