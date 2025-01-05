import random

print("Rock - Paper - Scissors")
choice = int(input("What do you chose? (0)Rock, (1)Paper, (2)Scissors: "))
comp = random.randint(0, 2)

print(comp)

if choice == 0:
    print("Your move: Rock")
    if comp == 0:
        print("Comp move: Rock")
        print("Tie!")
        exit()

    if comp == 1:
        print("Comp move: Paper")
        print("You lose!")
        exit()
    
    if comp == 2:
        print("Comp move: Scissors")
        print("You win!")
        exit()

if choice == 1:
    print("Your move: Paper")
    if comp == 0:
        print("Comp move: Rock")
        print("You win!")
        exit()
        
    if comp == 1:
        print("Comp move: Paper")
        print("Tie")
        exit()
    
    if comp == 2:
        print("Comp move: Scissors")
        print("You lose!")
        exit()

if choice == 2:
    print("Your move: Scissors")
    if comp == 0:
        print("Comp move: Rock")
        print("You lose!")
        exit()
        
    if comp == 1:
        print("Comp move: Paper")
        print("You win!")
        exit()
    
    if comp == 2:
        print("Comp move: Scissors")
        print("Tie!")
        exit()
