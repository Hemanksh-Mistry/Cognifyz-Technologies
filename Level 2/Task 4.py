# Task 4
# Task: Fibonacci Sequence
# Write a Python function that generates the Fibonacci sequence up to a given number of terms. The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.

# Function to generate the Fibonacci sequence
def fibonacci_sequence(n):
        a = 0
        b = 1
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, n):
                c = a + b
                print(c, end=' ')
                a = b
                b = c

# Taking the number of terms as input from the user
n = int(input("Enter the number of terms: "))
# Generating the Fibonacci sequence
fibonacci_sequence(n)