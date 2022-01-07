from menu import MenuItem, Menu
from sandwich_maker import SandwichMaker
from money_machine import MoneyMachine

sandwich_maker = SandwichMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) sandwich: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        sandwich_maker.report()
        money_machine.report()
    else:
        sandwich = menu.find_sandwich(choice)
        if sandwich_maker.is_resource_sufficient(sandwich) and money_machine.make_payment(sandwich.cost):
            sandwich_maker.make_sandwich(sandwich)