# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternD.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints this pattern if the input is 4
# 1 
# 1 2 2
# 1 2 2 3 3 3 
# 1 2 2 3 3 3 4 4 4 4 
#===================================================================================================

pattern_count = eval(input("Enter input for the pattern form: "))
for row in range(1, pattern_count + 2):
    for column in range(1, row):
        for number in range(column):
            print(column, end=" ")
    print()
