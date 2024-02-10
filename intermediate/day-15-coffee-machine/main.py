import data

status = "on"

def print_report():
    print(f'Water: {data.resources["water"]}ml')
    print(f'Milk: {data.resources["milk"]}ml')
    print(f'Coffee: {data.resources["coffee"]}g')
    print(f'Money: ${data.resources["money"]}')

def sufficient_resources(selection_par):
    if selection_par["ingredients"]["water"] > data.resources["water"]:
        print("Sorry, there is not enough water")
        return False
    elif selection_par["ingredients"]["coffee"] > data.resources["coffee"]:
        print("Sorry, there is not enough coffee")
        return False
    for key in selection_par["ingredients"]:
        if key == "milk":
            if selection_par["ingredients"]["milk"] > data.resources["milk"]:
                print("Sorry, there is not enough milk")
                return False
    else:
        return True

def calc_total_inserted(num_quarters, num_dimes, num_nickels, num_pennies):
    value_quarter = 0.25
    value_dime = 0.10
    value_nickel = 0.05
    value_penny = 0.01
    return num_quarters*value_quarter + num_dimes*value_dime + num_nickels*value_nickel + num_pennies*value_penny

def run_machine():
    print("running machine")
    #Process user's selection
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    valid_selection = False
    for key in data.MENU:
        if selection == key:
            selection = data.MENU[key]
            valid_selection = True
            print("selection matched")
    if not valid_selection:
        if selection == "off":
            global status
            status = "off"
            return
        elif selection == "report":
            print_report()
            return
        else:
            print("Invalid selection. Try again.")
            return

    #Check if sufficient resources
    if sufficient_resources(selection):

        #Prompt and input payment
        print(f'please pay ${selection["cost"]}')
        num_quarters = int(input("How many quarters?"))
        num_dimes = int(input("How many dimes?"))
        num_nickels = int(input("How many nickels?"))
        num_pennies = int(input("How many pennies?"))
        total_inserted = calc_total_inserted(num_quarters, num_dimes, num_nickels, num_pennies)

        #Determine if payment is sufficient
        if total_inserted == selection["cost"]:
            print("Accepted.")
        elif total_inserted > selection["cost"]:
            change = round(total_inserted - selection["cost"], 2)
            print(f"Accepted. Here is {change}")
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return
        data.resources["water"] -= selection["ingredients"]["water"]
        for key in selection["ingredients"]:
            if key == "milk":
                data.resources["milk"] -= selection["ingredients"]["milk"]
        data.resources["coffee"] -= selection["ingredients"]["coffee"]
        print(f"Here is your selection")
    else:
        return

while status == "on":
    print("run machine")
    run_machine()










