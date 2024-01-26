# Guess the Number Game

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Allow the player to make up to 5 guesses
for guess_count in range(1, 6):
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {guess_count} guesses.")
        break
else:
    print(f"Sorry, you ran out of guesses. The correct number was {secret_number}.")
