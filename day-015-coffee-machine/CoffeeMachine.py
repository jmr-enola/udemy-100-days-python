resources = [
    {"resource": "water", "val": 100, "unit": "ml", "unit_prefix": False},
    {"resource": "milk", "val": 50, "unit": "ml", "unit_prefix": False},
    {"resource": "water", "val": 76, "unit": "g", "unit_prefix": False},
    {"resource": "money", "val": 2.5, "unit": "$", "unit_prefix": True},
]

def startMachine():

    def checkResources(choice):

        recipes = {
            "espresso": [25, 0, 35],
            "latte": [10, 30, 20],
            "cappuccino": [20, 20, 20]
        }

        if choice not in recipes.keys():
            print("Invalid choice! Try again.")
            return False
        
        for i in range(3):
            if resources[i]["val"] < recipes[choice][i]:
                print(f"Sorry there is not enough {resources[i]['resource']}.")
                return False

        return True

    def checkPayment(choice, payment):

        prices = {
            "espresso": 1.5,
            "latte": 2.5,
            "cappuccino": 1.75,
        }

        if payment < prices[choice]:
            print("Sorry that's not enough money. Money refunded.")
            return False

        print("Payment sufficient. Processing order...")
        return True


    while (True): 
        
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning machine off...")
            exit()

        if choice == "report":
            for resource in resources:
                if resource["unit_prefix"]:
                    print(f'{resource["resource"]}: {resource["unit"]}{resource["val"]}')
                else:
                    print(f'{resource["resource"]}: {resource["val"]}{resource["unit"]}')
            continue

        if not checkResources(choice):
            continue

        print("Please insert coins... ")
        insertedCoins = {
            "quarters": int(input("quarters: ")),
            "dimes": int(input("dimes: ")),
            "nickles": int(input("nickles: ")),
            "pennies": int(input("pennies: ")),
        }

        payment = insertedCoins['quarters'] * 0.25 \
                + insertedCoins['dimes'] * 0.10    \
                + insertedCoins['nickles'] * 0.05  \
                + insertedCoins['pennies'] * 0.10
        
        checkPayment(choice, payment)




startMachine()

