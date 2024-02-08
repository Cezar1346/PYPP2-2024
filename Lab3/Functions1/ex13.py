name = input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
import random
luck = random.randrange(1, 20)
b = int(input("Take a guess."))
cnt = 1
if b != luck:
    while b != luck:
        if luck > b:
            print("Your guess is too low.") 
        elif luck < b:
            print("Your guess is too high.")
        b = int(input("Take a guess."))
        cnt += 1
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
else:
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")