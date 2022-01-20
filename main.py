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
    "money": 0,
}


def print_report(current_resources):
    """Prints report of available resources and money"""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}ml")
    print(f"Money: ${current_resources['money']}ml")


def check_resources(drink, current_resources):
    """Checks if there are enough resources to make the drink.
     Returns boolean value"""
    if drink == "espresso":
        if current_resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is no enough water")
            return False
        elif current_resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is no enough coffee")
            return False
        else:
            return True
    elif drink == "latte" or drink == "cappuccino":
        if current_resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is no enough water")
            return False
        elif current_resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is no enough coffee")
            return False
        elif current_resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is no enough milk")
            return True
        else:
            return True
    else:
        return False


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how man quarters?: "))
    dimes = int(input("how man dimes?: "))
    nickles = int(input("how man nickles?: "))
    pennies = int(input("how man pennies?: "))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_amount


def check_transaction(drink, amount):
    if MENU[drink]["cost"] > amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[drink]["cost"] < amount:
        print(f"Here is ${round(amount - MENU[drink]['cost'], 2)} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
        return True
    elif MENU[drink]["cost"] == amount:
        print(f"Here is your {drink} ☕. Enjoy!")
        return True
    else:
        return False


def process_drink(drink):
    global resources
    for resource in MENU[drink]["ingredients"]:
        resources[resource] -= MENU[drink]["ingredients"][resource]
    resources["money"] += MENU[drink]["cost"]


run_machine = "on"
while not run_machine == "off":
    run_machine = input("What would you like? (espresso/latte/cappuccino):").lower()
    if run_machine == "off":
        run_machine = "off"
    elif run_machine == "report":
        print_report(resources)
    elif run_machine == "espresso" or run_machine == "latte" or run_machine == "cappuccino":
        if check_resources(run_machine, resources):
            total = process_coins()
            if check_transaction(run_machine, total):
                process_drink(run_machine)
        else:
            run_machine = "off"
