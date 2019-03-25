# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 1, sum.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Asks the user for an integer and summates all of the numbers leading up to that number.
#===================================================================================================
    
summation = 0
user_specified_input = int(input("Enter Integer: "))
for number in range(1, user_specified_input+1):
    summation = summation + number
print("The sum of the first",user_specified_input,"positive integers is:",summation)

