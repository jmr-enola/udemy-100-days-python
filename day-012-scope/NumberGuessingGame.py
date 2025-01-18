import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

attempts = 0
difficulty = ""

while difficulty != 'easy' or difficulty != 'hard':
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    
    if difficulty.lower() == 'easy':
        attempts = 10
        break

    if difficulty.lower() == 'hard':
        attempts = 5
        break
    
    print("Invalid input!")

number = random.randint(1, 101)
guess = 0

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print("You guessed the number correctly. You win!")
        exit()

    if guess > number:
        print("Too high!\nGuess again.")
    
    if guess < number:
        print("Too low!\nGuess again.")

    attempts -= 1

print("You ran out of guesses. You lose!")


