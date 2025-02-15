from typing import List
from .Resource import Resource

class Coffee:
    def __init__(self, recipe:List[Resource], costPrice:float =0) -> None:
        self.recipe = recipe
        self.costPrice = costPrice

class Espresso(Coffee):
    def __init__(self):
        super().__init__([
            Resource("Water", 25, "ml"),
            Resource("Milk", 0, "ml"),
            Resource("Coffee", 35, "g")
        ], 1.5)

class Latte(Coffee):
    def __init__(self):
        super().__init__([
            Resource("Water", 10, "ml"),
            Resource("Milk", 30, "ml"),
            Resource("Coffee", 20, "g")
        ], 2.5)

class Cappuccino(Coffee):
    def __init__(self):
        super().__init__([
            Resource("Water", 20, "ml"),
            Resource("Milk", 20, "ml"),
            Resource("Coffee", 20, "g")
        ], 1.75)