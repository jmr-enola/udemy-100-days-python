resources = [
    {"resource": "Water", "val": 100, "unit": "ml", "unit_prefix": False},
    {"resource": "Milk", "val": 50, "unit": "ml", "unit_prefix": False},
    {"resource": "Water", "val": 76, "unit": "g", "unit_prefix": False},
    {"resource": "Water", "val": 2.5, "unit": "$", "unit_prefix": True},
]

def startMachine():
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

        if choice == "espresso":
            pass

        if choice == "latte":
            pass

        if choice == "cappuccino":
            pass


startMachine()

