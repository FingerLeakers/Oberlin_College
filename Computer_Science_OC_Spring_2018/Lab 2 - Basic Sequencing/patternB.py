# Author: Trevor Martin
# Date of Completion: 20 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, patternB.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program prints this pattern if the input is 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4 
#===================================================================================================

pattern_count = eval(input("Enter Input:"))
for row in range(1, pattern_count + 1):
    for column in range(1, pattern_count + 1):
        print(row, end = " ")  
    print()
