# Gabe Conner
# Assignment 8.2

import json

# JSON file name
json_file = r"C:\csd\csd-325\module-8\student_list.json"  # Would't read the file in the same folder, copy path to json file and insert here.

# A function to print the class list
def print_class_list(class_list, message):
    print(f"\n{message}")
    for student in class_list:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the JSON file into a Python list
try:
    with open(json_file, "r") as file:
        class_list = json.load(file)
except FileNotFoundError:
    print("JSON file not found. Creating a new one.")
    class_list = []

# Print the original list
print_class_list(class_list, "Original Student List:")

# Add a new student to the list
new_student = {
    "F_Name": "Gabe",
    "L_Name": "Conner",
    "Student_ID": 21387832,
    "Email": "GConner@my365.bellevue.edu"
}
class_list.append(new_student)

# Print the updated list
print_class_list(class_list, "Updated Student List:")

# Write the updated list back to the JSON file
with open(json_file, "w") as file:
    json.dump(class_list, file, indent=4)

print("\nThe .json file has been updated.")
