# Joshua Adrian O. Daet
# BSCpE 1-4
# Assignment 4 - Problem 2

# Open the file
with open("C:\assignments_oop\A4-Problem2/student_data.txt", "r") as file_handle:
    
    # Read the file line by line
    lines = file_handle.readlines()

# Initialize the highest GWA and name
highest_gwa = float('-inf')
highest_name = ""