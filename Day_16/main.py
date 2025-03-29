# #Day 16 Intermediate OOP - Creating tables using PyPi packages (prettytable)
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon",["Bulbasaur","Squirtle","Charmander","Pikachu"])
# table.add_column("Type",["Grass","Water","Fire","Electric"])
# table.align = "l"
#
# print(table)

# Coffee Machine OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create our machine, money handler, and menu once so their state persists.
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    # Ask the user for their drink choice, showing available options.
    user_input = input(f"What drink would you like ({menu.get_items()})?: ")

    if user_input == "report":
        # Display the current status of the machine and the money.
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink from the menu.
        fetched_item = menu.find_drink(user_input)

        if fetched_item:
            # Check if we have enough ingredients for the drink.
            if coffee_maker.is_resource_sufficient(fetched_item):
                print(f"You ordered {fetched_item.name}. That will be ${fetched_item.cost}.")

                # Process payment.
                transaction_successful = money_machine.make_payment(fetched_item.cost)
                print(transaction_successful)

                if transaction_successful:
                    # Make the drink and deduct the resources.
                    coffee_maker.make_coffee(fetched_item)
                else:
                    # Inform the user that the payment wasn't sufficient.
                    print(f"You entered an insufficient amount. Please enter {fetched_item.cost}")
            else:
                # Not enough resources to make the drink.
                print(f"Sorry, not enough resources available for the drink. The drink requires: {fetched_item.ingredients}.")
        else:
            # The drink is not in the menu.
            print("Sorry, that item is not available.")



