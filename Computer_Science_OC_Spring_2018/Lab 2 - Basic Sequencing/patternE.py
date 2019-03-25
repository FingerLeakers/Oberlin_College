# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternD.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints this pattern if the input is 3
# *****
# *
# *
# *
# ****
# *
# *
# *
# *****
#===================================================================================================

print("Pattern E Generator:")

user_input = int(input("Enter the index for your letter E: "))
for asterick in range(1, user_input + 3):
    print("*", end="")
print()

for asterick in range(1, user_input + 1):
    print("*")
    
for asterick in range(1, user_input + 2):
    print("*", end="")
print()

for asterick in range(1, user_input + 1):
    print("*")
    
for asterick in range(1, user_input + 3):
    print("*", end="")
print()
