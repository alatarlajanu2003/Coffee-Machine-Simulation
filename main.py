from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
game_on = True

while game_on:
    user_choice = input("What would you like?" + " " + menu.get_items())
    if user_choice == "off":
        game_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) == False:
        game_on = True
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink((user_choice))):
            if money_machine.make_payment(menu.find_drink((user_choice)).cost):
                coffee_maker.make_coffee(menu.find_drink((user_choice)))
        else:
            game_on = False
            
