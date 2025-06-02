#Gabe Conner
#Assignment 1.3
#5/31/2025

# We will first define a function within the program, here wer are defining the countdown_bottles function which will take the argument bottle_count. 
# Then the program will loop from bottle_count downt to 1 by counting backwards by -1 by finding the current number of bottles in each loop (i).
def countdown_bottles(bottle_count):
    for i in range(bottle_count, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i - 1} {'bottle' if i - 1 == 1 else 'bottles'} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

# The main program which will ask for the user input and then take that through the rest of the code.
try:
    bottles = int(input("How many bottles of beer are on the wall? "))
    if bottles > 0:
        countdown_bottles(bottles)
        print("Time to buy more bottles of beer.")
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Please enter a valid number.")
