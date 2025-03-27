# Day 15 - Coffee Machine Simulation

# Menu definition: drinks available, their ingredients, and cost
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

# Initial available resources in the machine
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500
}

# Total money collected from sales
money = 0
# Control flag to keep the machine running
switch = True

# Main loop to keep asking users for input
while switch:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # ESPRESSO LOGIC
    if user_input == "espresso":
        # Check if water and coffee are available at all
        if resources["water"] > 0 and resources["coffee"] > 0:
            # Define required ingredients
            water = 50
            coffee = 18

            # Check if enough resources are available
            if resources["water"] >= water and resources["coffee"] >= coffee:
                print("That will be $1.50. Please insert coins.")
                cost = 1.5

                # Ask for coin input
                user_input_quarters = input("How many quarters?: ")
                user_input_dimes = input("How many dimes?: ")
                user_input_nickles = input("How many nickles?: ")
                user_input_pennies = input("How many pennies?: ")

                # Calculate total money inserted
                total_money_input = (
                    int(user_input_quarters) * 0.25 +
                    int(user_input_dimes) * 0.1 +
                    int(user_input_nickles) * 0.05 +
                    int(user_input_pennies) * 0.01
                )

                # Not enough money
                if total_money_input < cost:
                    print(f"You input ${round(total_money_input, 2)}. "
                          f"There is a deficit of ${round(cost - total_money_input, 2)}. "
                          f"Here is your money back.")

                # Exact amount
                elif total_money_input == cost:
                    money += total_money_input
                    print("Thank you for inputting the exact amount! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee

                # More than needed: give change
                elif total_money_input > cost:
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. "
                          f"Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee

            else:
                # Not enough specific resources
                print("Not enough resources to make this drink.")
                if resources["water"] < water:
                    print("There is not enough water.")
                elif resources["coffee"] < coffee:
                    print("There is not enough coffee.")
        else:
            print("Not enough resources to make this drink.")

    # LATTE LOGIC
    elif user_input == "latte":
        if resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
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

                total_money_input = (
                    int(user_input_quarters) * 0.25 +
                    int(user_input_dimes) * 0.1 +
                    int(user_input_nickles) * 0.05 +
                    int(user_input_pennies) * 0.01
                )

                if total_money_input < cost:
                    print(f"You input ${round(total_money_input, 2)}. "
                          f"There is a deficit of ${round(cost - total_money_input, 2)}. "
                          f"Here is your money back.")

                elif total_money_input == cost:
                    money += total_money_input
                    print("Thank you for inputting the exact amount! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk

                elif total_money_input > cost:
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. "
                          f"Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk
            else:
                print("Not enough resources to make this drink.")
                if resources["water"] < water:
                    print("There is not enough water.")
                elif resources["coffee"] < coffee:
                    print("There is not enough coffee.")
                elif resources["milk"] < milk:
                    print("There is not enough milk.")
        else:
            print("Not enough resources to make this drink.")

    # CAPPUCCINO LOGIC
    elif user_input == "cappuccino":
        if resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
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

                total_money_input = (
                    int(user_input_quarters) * 0.25 +
                    int(user_input_dimes) * 0.1 +
                    int(user_input_nickles) * 0.05 +
                    int(user_input_pennies) * 0.01
                )

                if total_money_input < cost:
                    print(f"You input ${round(total_money_input, 2)}. "
                          f"There is a deficit of ${round(cost - total_money_input, 2)}. "
                          f"Here is your money back.")

                elif total_money_input == cost:
                    money += total_money_input
                    print("Thank you for inputting the exact amount! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk

                elif total_money_input > cost:
                    change = total_money_input - cost
                    money += cost
                    print(f"Thank you for your order! You entered: ${round(total_money_input,2)}. "
                          f"Here is your change: ${round(change, 2)}! Enjoy your drink!")
                    resources["water"] -= water
                    resources["coffee"] -= coffee
                    resources["milk"] -= milk
            else:
                print("Not enough resources to make this drink.")
                if resources["water"] < water:
                    print("There is not enough water.")
                elif resources["coffee"] < coffee:
                    print("There is not enough coffee.")
                elif resources["milk"] < milk:
                    print("There is not enough milk.")
        else:
            print("Not enough resources to make this drink.")

    # REPORT LOGIC
    elif user_input == "report":
        # Show current status of all resources and money
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(money))
