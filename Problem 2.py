# Joshua Adrian O. Daet
# BSCpE 1-4
# Assignment 4 - Problem 2

# Open the file
with open("C:/assignments_oop/A4-Problem2/student_data.txt", "r") as file_handle:
    
    # Read the file line by line
    lines = file_handle.readlines()

# Initialize the highest GWA and name
highest_gwa = float('-inf')
highest_name = ""

# Iterate over the lines
for line in lines:

    # Split the line into name and GWA
    parts = line.strip().split(",")
    if len(parts) == 2:
        name, gwa = parts
        try:

            # Convert the GWA to float
            gwa = float(gwa)

            # Compare the GWA with the highest GWA
            if gwa > highest_gwa :

                # Update the highest GWA and name
                highest_gwa = gwa
                highest_name = name
        except ValueError:
            # Handle the case where GWA is not a valid float
            print(f"Invalid GWA found for '{name}': '{gwa}'")

# Print the result
print("\033[34m\033[34mThe student with highest GWA\033[0m")
print("")
print("\033[31m\033[32mStudent Name:\033[0m", highest_name )
print("")
print("\033[31m\033[32mGWA:\033[0m", highest_gwa )
print("")
print("")

# Creating column for the names and GWA
print("Here is the list: ")
print("")
with open("C:/assignments_oop/TRYYY/student_data.txt") as column_file:
    print("\033[0;32m{:<30}{:<30}".format("Student Name:", "GWA:"))
    for line in column_file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            name, gwa = parts
            column_name = name
            column_gwa = gwa
            print("\033[0;38m{:<30}{:<30}".format(column_name, column_gwa))