from typing import List
from .Resource import Resource
from .Coffee import Espresso, Latte, Cappuccino

defaultResources = [
        Resource("Water", 100, "ml"),
        Resource("Milk", 50, "ml"),
        Resource("Coffee", 76, "g")
    ]

class CoffeeMachine:
    
    def __init__(self, resources:List[Resource] = defaultResources, money:float = 2.5) -> None:
        self.resources = resources
        self.money = money
        self.on = False
        self.choices = {
            "espresso": Espresso(),
            "latte": Latte(),
            "cappuccino": Cappuccino()
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

    def checkResource(self, order:str) -> bool:
        choice = self.choices[order]
        
        for i, resource in enumerate(self.resources):
            if resource.value < choice.recipe[i].value:
                print(f"Sorry there is not enough {resource.desc}.")
                return False
            
        return True
    
    def paymentProcess(self, order:str) -> bool:
        choice = self.choices[order]

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

        if payment < choice.costPrice:
            print("Sorry that's not enough money. Money refunded.")
            return False
        
        print("Payment sufficient. Processing order...")
        
        if payment > choice.costPrice:
            print(f'Here is ${payment - choice.costPrice} in change.')

        self.money += choice.costPrice

        return True
    
    def makeOrder(self, order:str) -> None:
        choice = self.choices[order]
        
        for i in range(len(choice.recipe)):
            self.resources[i].value -= choice.recipe[i].value

        print("Here is your coffee. Enjoy!\n")

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
            
            if not self.checkResource(order):
                print("Try another order.")
                continue

            if self.paymentProcess(order):
                self.makeOrder(order)