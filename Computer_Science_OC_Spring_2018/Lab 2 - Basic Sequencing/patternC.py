# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternC.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints this pattern if the input is 4
# 1 2 3 4
# 2 3 3 
# 3 3  
# 4
#===================================================================================================

user_input = int(input("Enter Input: "))
for row in range(1, user_input + 1):
    for column in range(row, n + 1):
        print(column, end = " ")    
    print()
