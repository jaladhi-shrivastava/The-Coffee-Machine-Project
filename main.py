import os
import time
menu = {
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

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# TODO: 1. Take user input about their choice of coffee and what to do next
def user_choice():
    """Get and validate user input for coffee selection or command."""
    while True:
        user_input=input("What would you like to have today?😋 (espresso/latte/cappuccino): ").lower().strip().replace(" ","")
        if user_input in ("espresso", "latte", "cappuccino", "report", "off"):
            return user_input
        else:
            print("Enter valid input.")


# TODO: 3. Check if the resources are sufficient
def check_resources(coffee_choice):
    """Check if we have sufficient resources to make the coffee"""
    for key, value in menu[coffee_choice]["ingredients"].items():
        if resources[key] < menu[coffee_choice]["ingredients"][key]:
            print(f"Sorry, the {key} is insufficient to make your coffee. Please Try again later.😔")
            return False
    return True

# TODO: 4. Update the resources according to the coffee, if sufficient.
def update_resources(coffee_choice):
    """Updates the ingredients of the coffee after making it """
    for k, v in resources.items():
        if k in menu[coffee_choice]["ingredients"]:
            resources[k] -= menu[coffee_choice]["ingredients"][k]


# TODO: 5. Process coins and convert them to dollars.
def process_coins():
    """Change coins to dollars."""
    print("Please insert your coins.🪙")
#Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    while True:
        try:
            quarters=int(input("How many quarters? "))*0.25
            dimes=int(input("How many dimes? "))*0.10
            nickles=int(input("How many nickles? "))*0.05
            pennies=int(input("How many pennies? "))*0.01
            dollars = quarters + dimes + nickles + pennies
            return dollars
        except ValueError:
            print("Enter valid input. Enter the number of coins.")

# TODO: 6. Process and handle payments.

def process_payment(coffee_choice,money):
    """Check if the money is sufficient and return change"""
    cost= menu[coffee_choice]["cost"]
    if money>= cost:
        if money> cost:
            change = round(money - cost, 2)
            print(f"Here's your change- ${change}🤑")
            print(f"Here is your {coffee_choice}.☕ Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


profit=0

# TODO: 2. Keep asking the question to user i.e execute the main loop of the game
def main_game():
    global profit
    coffee_machine=True
    print("WELCOME TO THE COFFEE MACHINE!!☕")
    print("Here is your menu:")
    for coffee, details in menu.items():
        print(f"{coffee.capitalize()}: ${details['cost']:.2f}")

    while coffee_machine:
        coffee=user_choice()
        if coffee=="report":
            report = [f"{item.capitalize()}: {amount}{units[item]}"
                for item, amount in resources.items() ]
            print('\n'.join(report))
            print(f"Money: ${profit:.2f}")
        elif coffee=="off":
            #Turn off the Coffee Machine by entering "off" to the prompt.
            print("Turning OFF.😴")
            coffee_machine=False
        else:
            check=check_resources(coffee_choice=coffee)
            if check:
                while True:
                    payment = process_payment(coffee_choice=coffee, money=process_coins())
                    if payment:
                        profit += menu[coffee]["cost"]
                        update_resources(coffee_choice=coffee)
                        break
                    else:
                        print("Try again!")
                        rerun = input("Do you want to insert coins again? Type 'Yes' or 'No'.").lower().strip().replace(" ", "")
                        if rerun != "yes":
                            print("THANK YOU FOR PLAYING. SEE YOU SOON! 🤗")
                            time.sleep(2)
                            clear()
                            break

            else:
                print("Try another coffee!")
                clear()
                continue

main_game()
