# Task 3
# Task: Password Strength Checker 
# Create a Python function that evaluates the strength of a password entered by the user. Implement checks for factors such as length, presence of uppercase and lowercase letters, digits, and special characters.

# Function to check the password strength
def password_strength(password):
        stat = []
        # Checking the length of the password
        if len(password) < 8:
                stat += ["Password length should be atleast 8 characters"]
        # Checking the presence of uppercase letters
        if not any(char.isupper() for char in password):
                stat += ["Password should contain atleast one uppercase letter"]
        # Checking the presence of lowercase letters
        if not any(char.islower() for char in password):
                stat += ["Password should contain atleast one lowercase letter"]
        # Checking the presence of digits
        if not any(char.isdigit() for char in password):
                stat += ["Password should contain atleast one digit"]
        # Checking the presence of special characters
        special_characters = "!@#$%^&*()-+"
        if not any(char in special_characters for char in password):
                stat += ["Password should contain atleast one special character"]
        # If all the conditions are satisfied
        if len(stat) == 0:
                print ("Strong Password")
        else:
                print ("Weak Passwoord: ")
                for i in stat:
                        print(i)

# Taking the password as input from the user
password = input("Enter the password: ")
# Checking the password strength
password_strength(password)