# #Day 16 Intermediate OOP
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon",["Bulbasaur","Squirtle","Charmander","Pikachu"])
# table.add_column("Type",["Grass","Water","Fire","Electric"])
# table.align = "l"
#
# print(table)

# Coffee Machine

MENU = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
     "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000
}

money = 0
switch = True

while switch:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso":
        print("That will be $1.50. Please insert coins.")
        cost = 1.5

        user_input_quarters = input("How many quarters?: ")
        user_input_dimes = input("How many dimes?: ")
        user_input_nickles = input("How many nickles?: ")
        user_input_pennies = input("How many pennies?: ")

        total_money_input = (int(user_input_quarters) * 0.25) + (int(user_input_dimes) * 0.1) + (
                    int(user_input_nickles) + 0.05) + (int(user_input_pennies) * 0.01)

        if total_money_input < cost:
            # Finance
            print(
                f"You input ${round(total_money_input, 2)}. There is a deficit of ${round(cost - total_money_input, 2)}. Here is the money your money back ${round(total_money_input, 2)} - Please input at least ${round(cost, 2)}.")

        elif cost == total_money_input:
            # Finance
            money += total_money_input
            print(f"Thank you for inputting the exact amount! Enjoy your drink!")
            # Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150


        elif total_money_input > cost:
            # Finance
            change = total_money_input - cost
            money += cost
            print(f"Thank you for your order! Here is your ${round(change, 2)}! Enjoy your drink!")
            # Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150


    elif user_input == "latte":
        print("That will be $2.50. Please insert coins.")
        cost = 2.5
        user_input_quarters = input("How many quarters?: ")
        user_input_dimes = input("How many dimes?: ")
        user_input_nickles = input("How many nickles?: ")
        user_input_pennies = input("How many pennies?: ")

        total_money_input = (int(user_input_quarters) * 0.25) + (int(user_input_dimes) * 0.1) + (int(user_input_nickles) + 0.05) + (int(user_input_pennies) * 0.01)

        if total_money_input < cost:
            # Finance
            print(f"You input ${round(total_money_input,2)}. There is a deficit of ${round(cost-total_money_input,2)}. Here is the money your money back ${round(total_money_input,2)} - Please input at least ${round(cost,2)}.")

        elif cost == total_money_input:
            # Finance
            money += total_money_input
            print(f"Thank you for inputting the exact amount! Enjoy your drink!")
            #Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150


        elif total_money_input > cost:
            # Finance
            change = total_money_input - cost
            money += cost
            print(f"Thank you for your order! Here is your ${round(change,2)}! Enjoy your drink!")
            # Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150


    elif user_input == "cappuccino":
        print("That will be $3.00. Please insert coins.")
        cost = 3.0
        user_input_quarters = input("How many quarters?: ")
        user_input_dimes = input("How many dimes?: ")
        user_input_nickles = input("How many nickles?: ")
        user_input_pennies = input("How many pennies?: ")

        total_money_input = (int(user_input_quarters) * 0.25) + (int(user_input_dimes) * 0.1) + (
                    int(user_input_nickles) + 0.05) + (int(user_input_pennies) * 0.01)

        if total_money_input < cost:
            # Finance
            print(
                f"You input ${round(total_money_input, 2)}. There is a deficit of ${round(cost - total_money_input, 2)}. Here is the money your money back ${round(total_money_input, 2)} - Please input at least ${round(cost, 2)}.")

        elif cost == total_money_input:
            # Finance
            money += total_money_input
            print(f"Thank you for inputting the exact amount! Enjoy your drink!")
            # Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150


        elif total_money_input > cost:
            # Finance
            change = total_money_input - cost
            money += cost
            print(f"Thank you for your order! Here is your ${round(change, 2)}! Enjoy your drink!")
            # Resource depletion for making the drink
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150

    elif user_input == "report":
        print("Water: " + str(resources["water"]) +"ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: " + "$" + str(money))


# Coffee Machine OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



