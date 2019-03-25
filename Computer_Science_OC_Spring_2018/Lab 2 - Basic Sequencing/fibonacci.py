# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, fibonacci.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program finds the nth fibonacci number. 
#===================================================================================================

nth_fib_number = int(input("Please pick a fibonacci number greater than 2: "))
previous_num = 1
current_num = 1

for fib_number in range(nth_fib_number - 2):
    current_num = (current_num + previous_num)
    previous_num = (current_num - previous_num)
    
print("The",nth_fib_number,"number in the Fibonacci Sequence is:",current_num)


