from menu import beverage, resources


def report():
    for key, item in resources.items():
        print(f"{key.capitalize()}: {item}")


def get_drink() -> str:
    choice = input("What would you like? (cappuccino/espresso/latte): ").lower()

    while choice not in beverage.keys():
        print(f"Sorry. {choice.capitalize()} not available!")
        choice = input("What would you like? (cappuccino/espresso/latte): ").lower()
        if choice == 'q':
            print("Goodbye")
            return

    return choice


def check_resource(drink):
    print(f"You chose {drink}")


def main():
    user_drink = get_drink()
    check_resource(drink=user_drink)


if __name__ == "__main__":
    main()