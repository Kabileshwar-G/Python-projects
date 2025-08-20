# Number Guessing Game
import random

random_number = random.randint(1, 10)  # You can change this
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 10.")
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == random_number:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
print("Sorry, you've run out of attempts. The number was", random_number)
