from arts.day_13_art import MENU, resources

menu = MENU
resources = resources
profit = 0


def report():
    print(f"WATER: {resources['water']}ml")
    print(f"MILK: {resources['milk']}ml")
    print(f"COFFEE: {resources['coffee']}g")
    print(f"MONEY: ${profit:.2f}")


def money():
    print("Please insert coins")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nick = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))

    return (quarter * 0.25) + (dime * 0.10) + (nick * 0.05) + (penny * 0.01)


def check_cost(user_money, drink):
    if user_money >= drink["cost"]:
        change = round(user_money - drink["cost"], 2)
        print(f"Here is ${change} in change.")
        return True
    print("Sorry, that's not enough money. Money refunded.")
    return False


def check_ingredients(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def minus_ingredients(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


def coffee():
    global profit
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off... ☕")
            break

        if choice == "report":
            report()

        elif choice in menu:
            drink = menu[choice]
            if check_ingredients(drink["ingredients"]):
                payment = money()
                if check_cost(payment, drink):
                    minus_ingredients(drink["ingredients"])
                    profit += drink["cost"]
                    print(f"Here is your {choice} ☕ Enjoy!")

        elif choice == "cancel":
            print("Cancelling order...")
            coffee()

        else:
            print("Invalid option. Try again!")


coffee()
