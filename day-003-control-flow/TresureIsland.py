print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

move = input("Is it (1)left or (2)right? ")

if move != '1':
    print("Game Over")
    exit()

move = input("Do you (1)swim or (2)wait? ")

if move != '2':
    print("Game Over!")
    exit()

move = input("Which door? (1)Red, (2)Blue or (3)Yellow? ")

if move != '3':
    print("Game Over!")
    exit()

print("You win!!!")
