from typing import List
from Resource import Resource

defaultResources = [
            Resource("Water", 100, "ml"),
            Resource("Milk", 50, "ml"),
            Resource("Coffee", 76, "g")
        ]

class CoffeeMachine:
    
    def __init__(self, resources: List[Resource] = defaultResources, money: float = 2.5) -> None:
        self.resources = resources
        self.money = money
        self.on = False
        self.choices = {
            "espresso": None,
            "latte": None,
            "cappuccino": None
        }

    def machineOff(self) -> None:
        self.on = False
        print("Turning off...")

    def printReport(self) -> None:

        print("\n---Generated Report---")

        for resource in self.resources:
            print(f"{resource.desc}: {resource.value}{resource.unit}")

        print(f"Money: ${self.money}")
        print("----End  Of Report----\n")

    def machineOn(self) -> None:
        
        self.on = True

        while(self.on):
            order = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if order == "off":
                self.machineOff()
                continue
                
            if order == "report":
                self.printReport()
                continue

            if order not in self.choices.keys():
                print("Sorry can't process order. Invalid keyword, please try again.")
                continue
            
            else:
                pass

