# Task 5
# Task: File Manipulation 
# Write a Python program that reads a text file and counts the occurrences of each word in the file. Display the results in alphabetical order along with their respective counts.

# Function to count the occurrences of each word in the file
def count_words(file_name):
        # Opening the file in read mode
        with open(file_name, 'r') as file:
                # Reading the contents of the file
                data = file.read()
                # Splitting the contents of the file into words
                words = data.split()
                # Creating a dictionary to store the count of each word
                word_count = {}
                # Counting the occurrences of each word
                for word in words:
                        if word in word_count:
                                word_count[word] += 1
                        else:
                                word_count[word] = 1
                # Sorting the dictionary based on keys
                sorted_word_count = dict(sorted(word_count.items()))
                # Displaying the results
                for word, count in sorted_word_count.items():
                        print(f"{word}: {count}")

# Taking the file name as input from the user
file_name = input("Enter the file name: ")
# Counting the occurrences of each word in the file
count_words(file_name)