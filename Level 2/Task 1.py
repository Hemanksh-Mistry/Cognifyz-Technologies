# Task 1
# Task: Guessing Game
# Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number. The program should provide hints such as "too high" or "too low" until the correct number is guessed.

import random

def guessing_game():
        number = random.randint(1, 100)
        print ("I'm thinking of a number between 1 and 100")
        guess = int(input("Enter your guess: "))
        while guess != number:
                if number - guess > 20:
                        print("Too low")
                        guess = int(input("Enter your guess: "))
                elif number - guess > 10:
                        print("Low")
                        guess = int(input("Enter your guess: "))
                elif number - guess > 5:
                        print("Close but low")
                        guess = int(input("Enter your guess: "))
                elif guess - number > 20:
                        print("Too high")
                        guess = int(input("Enter your guess: "))
                elif guess - number > 10:
                        print("High")
                        guess = int(input("Enter your guess: "))
                elif guess - number > 5:
                        print("Close but high")
                        guess = int(input("Enter your guess: "))
                else:
                        print("Very close")
                        guess = int(input("Enter your guess: "))
        print("Congratulations! You guessed the number correctly.")

guessing_game()