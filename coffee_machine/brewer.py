from properties import beverage, resources


class CoffeeMaker:

    def __init__(self, funds: float = 0.0) -> None:
        self.water, self.milk, self.coffee = [*resources.values()]
        self.funds = funds

    def choose_drink(self, drink):
        self.drink = drink
        self.cost = beverage.get(self.drink).get('cost')

    def insert_coins(self, amt_paid):
        self.amt_paid = amt_paid

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
        "\nCoffee Maker Resource Levels:\n"
        f"Water : {self.water}ml\n"
        f"Milk  : {self.milk}ml\n"
        f"Coffee: {self.coffee}g\n"
        f"Money : ${self.funds:.2f}")

        print(resource_levels)
