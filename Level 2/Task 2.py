# Task 2
# Task: Number Guesser
# Create a number guessing game where the program generates a random number between a specified range, and the user tries to guess it. Provide feedback to the user if their guess is too high or too low.

import random

def guessing_game():
        l_range = int(input("Enter the lower limit of the range: "))
        u_range = int(input("Enter the upper limit of the range: "))
        number = random.randint(l_range, u_range)
        print ("I'm thinking of a number between " + str(l_range) + " and " + str(u_range) + ".")
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