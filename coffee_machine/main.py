from properties import beverage, resources


class CoffeeMaker:

    def __init__(self, drink: str, money: float = 2.50) -> None:
        self.drink = drink
        self.water, self.milk, self.coffee = [*resources.values()]
        self.money = money


    def make_coffee(self):
        water, milk, coffee = beverage.get(self.drink).get('ingredients').values()

        def check_resource(self):
            if water > self.water:
                print("Insufficient Water")
            elif milk > self.milk:
                print("Insufficient Milk")
            elif coffee > self.coffee:
                print("Insufficient coffee")
            return self.water >= water and self.milk >= milk and self.coffee >= coffee

        if check_resource(self):
            print(f"Brewing a delicous {self.drink.capitalize()}...")
            self.water -= water
            self.milk -= milk
            self.coffee -= coffee

    def status_report(self):
        resource_levels = (
        "Coffee Maker Resource Levels:\n"
        f"Water : {self.water}ml\n"
        f"Milk  : {self.milk}ml\n"
        f"Coffee: {self.coffee}g\n"
        f"Money : ${self.money:.2f}")

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


def main():

    user_drink = get_drink()
    if user_drink:
        machine = CoffeeMaker(user_drink)
        machine.status_report()
        print(machine.water)
        machine.make_coffee()
        machine.status_report()


if __name__ == "__main__":
    main()