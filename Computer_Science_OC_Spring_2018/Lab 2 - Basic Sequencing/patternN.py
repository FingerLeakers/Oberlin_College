# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternD.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints this pattern if the input is 3
# *  *
# ** *
# * **
# *  *
#===================================================================================================

print("Pattern N Generator:")
user_input = int(input("Enter the index (must be greater than 2) for your N pattern: "))

if user_input < 2:
    print("Please enter an integer 2 or greater.")
    
else:
    print("*", end="")
    for iteration in range(1, user_input + 1):
        print(" ", end="")
    print("*", end="")
    print()

    for iteration in range(1, user_input+1):
        print("*", end="")
        for iteration2 in range(1, user_input + 1):
            if iteration2 == iteration:
                print("*", end="")
            else:
                print(" ", end="")
        print("*", end="")
        print()
                
    print("*", end="")
    for iteration in range(1, user_input + 1):
        print(" ", end="")
    print("*", end=" ")
    print()
