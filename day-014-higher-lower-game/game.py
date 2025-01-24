from display import logo, vs
from data import data
import random
import os

def round(data_a, data_b):
    print(f'Compare A: {data_a["name"]}, {data_a["description"]}, from {data_a["country"]}')
    print(vs)
    print(f'Compare B: {data_b["name"]}, {data_b["description"]}, from {data_b["country"]}')
    response = ""
    
    while True:
        response = input("Who has more follower? Type 'A' or 'B': ").upper()
        
        if response == 'A' or response == 'B':
            break

        print("Invalid input. Please try again!")

    if response == 'A' and data_a["follower_count"] >= data_b["follower_count"]:
        return data_a
    
    if response == 'B' and data_b["follower_count"] >= data_a["follower_count"]:
        return data_b
    
    return False

def getRandomData():
    return data[random.randint(0, len(data) - 1)]

data_a = getRandomData()
data_b = getRandomData()
score = 0

print(logo)

while True:
    result = round(data_a, data_b)
    os.system('cls||clear')
    print(logo)
    
    if result == False:
        break
    
    score += 1
    print(f"You are right! Current score: {score}")

print(f"You got it wrong! Final score: {score}")

