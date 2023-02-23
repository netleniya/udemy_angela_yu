from brewer import CoffeeMaker
from properties import beverage, coins
import sys


def get_choice() -> str:
    """get choice of drink from user input

    Returns:
        str: drink choice
    """
    choice = input("What would you like? (Cappuccino/Espresso/Latte) or 'Q' to quit: ").lower()

    while choice not in beverage.keys():
        if choice in ('q', 'Q'):
            sys.exit("Exiting...")
        print(f"Sorry. {choice} not offered at the moment!")
        choice = input("Choose either Cappuccino/Espresso/Latte) or 'Q' to quit: ").lower()

    return choice


def insert_coins() -> float:
    """Prompt user to insert different coin denominations. Return Total

    Returns:
        float: total money inserted
    """
    total = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))

    total += quarters * coins.get('quarters') + dimes * coins.get('dimes') + nickels * coins.get('nickles')
    return total


def main():
    """main function loop
    """
    machine_on = True
    machine = CoffeeMaker()

    while machine_on:
        user_drink = get_choice()
        amt_paid = insert_coins()

        if user_drink:
            machine.choose_drink(user_drink)
            machine.insert_coins(amt_paid)
            machine.make_coffee()

            if machine.water <= 0:
                sys.exit("Water Depleted. Exiting")


if __name__ == "__main__":
    main()
