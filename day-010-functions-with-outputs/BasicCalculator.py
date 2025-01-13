import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while (True):

    posible_operations = ["+", "-", "*", "/"]
    operation = ""
    num1 = 0
    num2 = 0
    result = 0
    carry_over = ""

    num1 = float(input("What's the first number? "))

    

    while(True):

        operation = ""

        print("+\n-\n*\n/")
        while operation not in posible_operations:
            operation = input("Pick and operation: ")
            if operation not in posible_operations:
                print("Operation invalid. Please select a valid operation.")

        num2 = float(input("What's the next number? "))

        if operation == "+":
            result = add(num1, num2)

        if operation == "-":
            result = subtract(num1, num2)

        if operation == "*":
            result = multiply(num1, num2)

        if operation == "/":
            result = divide(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")
        carry_over = input(f"Type 'y' if you want to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if carry_over.lower() == 'y':
            num1 = result
            continue

        if carry_over.lower() == 'n':
            num1 = 0
            os.system('cls||clear')
            break

        exit()

         


