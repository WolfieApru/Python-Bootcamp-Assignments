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

# Coffee Machine OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
switch = True

while True:
    user_input = input("What drink would you like (latte, espresso, cappuccino)?: ")

    menu = Menu()

    fetched_item = menu.find_drink(user_input)

    if fetched_item:
        print(fetched_item.name)
        print(fetched_item.cost)
        print(fetched_item.ingredients)
    else:
        print("Sorry, that item is not available.")

# menu = Menu()
# print(menu.get_items())



