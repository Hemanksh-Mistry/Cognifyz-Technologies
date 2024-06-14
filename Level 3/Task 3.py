# Task 3
# Task: Automate a Task
# Identify a repetitive task, such as data processing, file management, or report generation, and develop a script to automate it using Python. This task will showcase their problem-solving skills and familiarity with Python's automation capabilities.

# Automating the task of renaming multiple files in a directory

# Importing the required libraries
import os

# Function to rename files in a directory
def rename_files(directory_path):
        # Changing the current working directory
        os.chdir(directory_path)
        # Listing all files in the directory
        files = os.listdir()
        # Renaming each file
        for index, file in enumerate(files):
                # Constructing the new file name
                new_name = f"file_{index+1}.txt"
                # Renaming the file
                os.rename(file, new_name)
        print("Files renamed successfully!")

# Taking the directory path as input from the user
directory_path = input("Enter the directory path: ")
# Renaming the files in the directory
rename_files(directory_path)