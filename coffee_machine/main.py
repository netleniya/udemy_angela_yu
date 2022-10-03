from properties import beverage, coins, resources


class CoffeeMaker:

    def __init__(self, drink: str, amt_paid:int, funds: float = 2.50) -> None:
        self.drink = drink
        self.water, self.milk, self.coffee = [*resources.values()]
        self.cost = beverage.get(self.drink).get('cost')
        self.amt_paid = amt_paid
        self.funds = funds


    def make_coffee(self) -> None:
        """brew coffee if there is enough money and sufficient resources

        Returns:
            None: None
        """
        water, milk, coffee = beverage.get(self.drink).get('ingredients').values()

        def check_price(self) -> bool:
            if self.amt_paid < self.cost:
                print(f"Sorry, that's not enough money. ${self.amt_paid:.2f} refunded")
            return self.amt_paid >= self.cost

        change = self.amt_paid - self.cost

        if check_price(self):
            def check_resource(self) -> bool:
                if water > self.water:
                    print("Sorry there seems to be insufficient water")
                elif milk > self.milk:
                    print("Sorry there is not enough nsufficient milk")
                elif coffee > self.coffee:
                    print("Sorry, insufficient coffee")
                return self.water >= water and self.milk >= milk and self.coffee >= coffee

            if check_resource(self):
                print(f"Brewing a delicous {self.drink.capitalize()}...")
                self.water -= water
                self.milk -= milk
                self.coffee -= coffee
                self.funds += self.cost
                print(f"Your change is ${change:.2f}. Enjoy!")
            else:
                print(f"Your ${self.amt_paid} has been refunded.")


    def __status_report(self) -> None:
        """get a status report on resource and money levels in machine
        """
        resource_levels = (
        "Coffee Maker Resource Levels:\n"
        f"Water : {self.water}ml\n"
        f"Milk  : {self.milk}ml\n"
        f"Coffee: {self.coffee}g\n"
        f"Money : ${self.funds:.2f}")

        print(resource_levels)


def get_drink() -> str:
    choice = input("What would you like? (Cappuccino/Espresso/Latte): ").lower()

    while choice not in beverage.keys():
        if choice in ('q', 'Q'):
            print("Exiting...")
            return
        print(f"Sorry. {choice} not offered at the moment!")
        choice = input("Choose either Cappuccino/Espresso/Latte): ").lower()

    return choice


def insert_coins():
    total = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))

    total = quarters * coins.get('quarters') + dimes * coins.get('dimes') + nickels * coins.get('nickles')
    return total


def main():

    user_drink = get_drink()
    amt_paid = insert_coins()

    if user_drink:
        coffee = CoffeeMaker(user_drink, amt_paid)

        coffee._CoffeeMaker__status_report()
        coffee.make_coffee()

        print("Check Levels after:\n")
        coffee._CoffeeMaker__status_report()



if __name__ == "__main__":
    main()