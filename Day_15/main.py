
# Day 15 Coffee Machine
#Given:
##################################################################
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
    "water": 500,
    "milk": 500,
    "coffee": 500
}
##################################################################
#The objective is to create logic for a coffee machine using conditionals - refer Coffee+Machine+Program+Requirements.pdf

money = 0
switch = True

while switch:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso":

        if resources["water"] > 0 and resources["coffee"] > 0:
            #Recipe
            water = 50
            coffee = 18

            if resources["water"] >= water and resources["coffee"] >= coffee:

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
                        f"You input ${round(total_money_input, 2)}. There is a deficit of ${round(cost - total_money_input, 2)}. Here is the money your money back: ${round(total_money_input, 2)} - Please input at least ${round(cost, 2)}.")

                elif cost == total_money_input:
                    # Finance
                    money += total_money_input
                    print(f"Thank you for inputting the exact amount! Enjoy your drink!")
                    # Resource depletion for making the drink
                    resources["water"] -= water
                    resources["coffee"] -= coffee

                elif total_money_input > cost:
                    # Finance
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    # Resource depletion for making the drink
                    resources["water"] -= water
                    resources["coffee"] -= coffee

            else:
                print(f"Not enough resources to make this drink: {resources}")

                if resources["water"] <= water:
                    print("There is not enough water.")

                elif resources["coffee"] <= coffee:
                    print("There is not enough coffee.")
        else:
            print(f"Not enough resources to make this drink: {resources}")

    elif user_input == "latte":
        if resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
            # Recipe
            water = 200
            coffee = 24
            milk = 150

            if resources["water"] >= water and resources["coffee"] >= coffee and resources["milk"] >= milk:

                print("That will be $2.50. Please insert coins.")
                cost = 2.5

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
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk


                elif total_money_input > cost:
                    # Finance
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    # Resource depletion for making the drink
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk
            else:
                print(f"Not enough resources to make this drink: {resources}")

                if resources["water"] <= water:
                    print("There is not enough water.")

                elif resources["coffee"] <= coffee:
                    print("There is not enough coffee.")

                elif resources["milk"] <= milk:
                    print("There is not enough milk.")
        else:
            print(f"Not enough resources to make this drink: {resources}")



    elif user_input == "cappuccino":
        if resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
            # Recipe
            water = 250
            coffee = 24
            milk = 100

            if resources["water"] >= water and resources["coffee"] >= coffee and resources["milk"] >= milk:

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
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk


                elif total_money_input > cost:
                    # Finance
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    # Resource depletion for making the drink
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk
            else:
                print(f"Not enough resources to make this drink: {resources}")

                if resources["water"] <= water:
                    print("There is not enough water.")

                elif resources["coffee"] <= coffee:
                    print("There is not enough coffee.")

                elif resources["milk"] <= milk:
                    print("There is not enough milk.")
        else:
            print(f"Not enough resources to make this drink: {resources}")

    #Report
    elif user_input == "report":
        print("Water: " + str(resources["water"]) +"ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: " + "$" + str(money))




