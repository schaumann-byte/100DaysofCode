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

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


# TODO1: Print report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def update_resources(order):
    for ingredient in MENU[order]['ingredients']:
        resources[ingredient] -= MENU[order]['ingredients'][ingredient]


def check_ingredient(order, ingredient):
    if MENU[order]['ingredients'][ingredient] > resources[ingredient]:
        return True


# TODO2: Check resources
def check_resources(order):
    if order == 'espresso':
        if check_ingredient(order, 'water'):
            print("Sorry, there's not enough water")
            return False
        elif check_ingredient(order, 'coffee'):
            print("Sorry, there's not enough coffee")
            return False
    if order == 'latte' or order == 'cappuccino':
        if check_ingredient(order, 'water'):
            print("Sorry, there's not enough water")
            return False
        elif check_ingredient(order, 'milk'):
            print("Sorry, there's not enough milk")
            return False
        elif check_ingredient(order, 'coffee'):
            print("Sorry, there's not enough coffee")
            return False


# TODO3: Check money
def check_money(quarters, dimes, nickles, pennies, order):
    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total_money >= MENU[order]['cost']:
        change = total_money - MENU[order]['cost']
        update_resources(order)
        print(f"Here's your change {round(change,2)}")
        print(f"Enjoy your {order} :)")
        resources['money'] += MENU[order]['cost']
    else:
        print("That's not enough money, money refunded")
        return False


continuar = True
while continuar:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        break
    if choice != 'report':
        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            if check_resources(choice) != False:
                print("Please insert coins. ")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                if check_money(quarters, dimes, nickles, pennies, choice) == False:
                    pass
            else:
                pass
        else:
            print("Opção invalida")
    else:
        report()
