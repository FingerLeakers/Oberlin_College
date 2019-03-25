# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 1, factorial.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program finds the factorial of a number.
#===================================================================================================

factorial = 1

user_specified_input = int(input("Enter Integer: "))

for number in range(1, user_specified_input + 1):
    factorial = factorial * number
    
print("The factorial of",user_specified_input,"is", factorial)


