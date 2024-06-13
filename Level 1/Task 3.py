# Task 3
# Task: Email Validator
# Develop a Python function that validates whether a given string is a valid email address. Implement checks for the format, including the presence of an "@" symbol and a domain name

import re

def email_validator(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return True
        else:
                return False

email = input("Enter an email address: ")

if email_validator(email):
        print("Valid email address")
else:
        print("Invalid email address")