from menu import beverage, resources

def get_drink() -> str:
    prompt = input("What would you like? (cappuccino/espresso/latte): ").lower()

    if prompt == 'q':
        print("Goodbye!")
        return None
    elif prompt in beverage.keys():
        return prompt
    else:
        print(f"Sorry. {prompt.capitalize()} not available!")
        get_drink()

