import random

letters = "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like your password? "))
nr_symbols = int(input("How many symbols would you like your password? "))
nr_numbers = int(input("How many numbers would you like your password? "))

total = nr_letters + nr_symbols + nr_numbers
password = []
n = 0

while (total > 0):    

    total = nr_letters + nr_symbols + nr_numbers

    #choices 0 = letters, 1 = symbols, 2 = numbers
    choice = random.randint(0, 2)
    
    if choice == 0 and nr_letters > 0:
        password.append(letters[random.randint(0, len(letters) - 1)])
        nr_letters -= 1

    if choice == 1 and nr_symbols  > 0:
        password.append(symbols[random.randint(0, len(symbols) - 1)])
        nr_symbols -= 1

    if choice == 2 and nr_numbers  > 0:
        password.append(numbers[random.randint(0, len(numbers) - 1)])
        nr_numbers -= 1

print("password: " + "".join(password))