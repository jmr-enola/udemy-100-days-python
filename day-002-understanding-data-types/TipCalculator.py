print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
nPerson = float(input("How many person should pay? "))
payment = bill * (100 + tip) / 100 / nPerson
print(f'Each person should pay: ${payment}')
