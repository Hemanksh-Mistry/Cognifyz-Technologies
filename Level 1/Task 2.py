# Task 2
# Task: Temperature Conversion
# Create a Python program that converts temperatures between Celsius and Fahrenheit. Prompt the user to enter a temperature value and the unit of measurement, and then display the converted temperature.

while True:
        print ("Menu")
        print ("1. Celcius to Fahrenheit")
        print ("2. Fahrenheit to Celcius")
        print ("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
                c = float(input("Enter the temperature in Celcius: "))
                f = (c * 9/5) + 32
                print (f, "F")
        elif choice == 2:
                f = float(input("Enter the temperature in Fahrenheit: "))
                c = (f - 32) * 5/9
                print (c, "C")
        elif choice == 3:
                exit()
        else:
                print ("Invalid choice")