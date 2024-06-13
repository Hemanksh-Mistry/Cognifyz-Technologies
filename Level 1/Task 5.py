# Task 5
# Task: Palindrome Checker
# Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward (e.g., "madam" or "racecar").

a = input("Enter a string: ")
if a == a[::-1]:
    print("The string is a palindrome")
else:
        print("The string is not a palindrome")