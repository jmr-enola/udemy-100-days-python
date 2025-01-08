import random

words = [
    'cammel',
    'boots',
    'rock'
]

#choose a random word
word = list(words[random.randint(0, len(words) - 1)])
guese = list("_" * len(word))
max_lives = 6
lives = 6
has_guesed = False

while (lives > 0 and not has_guesed):
    print(f'**********{lives}/{max_lives}*************')
    print(f'word: {"".join(guese)}')
    letter = input('Guese as letter: ').lower()

    if letter not in word or letter == "_":
        lives -= 1
        continue

    while letter in word:
        index = word.index(letter)
        guese[index] = letter
        word[index] = "_"
    
    if "_" not in guese:
        has_guesed = True

if lives == 0:
    print('You lose...')

if has_guesed:
    print('You win!')
