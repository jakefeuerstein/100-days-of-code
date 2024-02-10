from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Create objects
drink_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

def process_order():
    #Input drink order
    drink_order = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    #Process drink order or other
    if drink_order in drink_menu.get_items():
        drink_order = drink_menu.find_drink(drink_order)
    elif drink_order == "off":
        global machine_on
        machine_on = False
        return
    elif drink_order == "report":
        coffee_maker.report()
        money_machine.report()
        return
        #Exit loop
    else:
        print("Invalid entry.")
        #Exit loop

    #Check resources
    if coffee_maker.is_resource_sufficient(drink_order):
        #Process payment
        if money_machine.make_payment(drink_order.cost):
            coffee_maker.make_coffee(drink_order)

while machine_on:
    process_order()