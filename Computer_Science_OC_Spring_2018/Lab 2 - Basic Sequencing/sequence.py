# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternD.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints a sequence leading up to a number n of squared integers
#===================================================================================================

user_input = int(input("Enter integer number for your sequence: "))

print("Squares from",user_input**2,"down to 1: ")

for iteration in range(user_input, 0, -1):
    print(iteration**2," ",end="")


