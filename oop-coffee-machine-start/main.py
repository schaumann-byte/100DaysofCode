from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#1: Criar Objetos
waiter = CoffeeMaker()

order = Menu()

cashier = MoneyMachine()

continuar = True
while continuar:
    choice = input(f'What would you like? {order.get_items()}: ')
    if choice == 'off':
        continuar = False
    elif choice == "report":
        CoffeeMaker.report(waiter)
        MoneyMachine.report(cashier)
    else:
        drink = order.find_drink(choice)
        if waiter.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
                waiter.make_coffee(drink)
        else:
            print("Opção invalida")