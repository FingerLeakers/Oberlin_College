# Author: Trevor Martin
# Date of Completion: 20 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, interest.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program calculates compounded monthly interest.
#===================================================================================================

user_inputted_month = eval(input("Enter # of Months: "))
user_inputted_balance = eval(input("Enter your initial savings: "))
user_inputted_interest_rate = eval(input("Enter the monthly interest: "))
user_inputted_monthly_contr = eval(input("Enter your monthly contribution: "))
new_balance = user_inputted_balance
for month in range(1, user_inputted_month + 1):
    interest = new_balance * user_inputted_interest_rate
    new_balance = new_balance + interest
    new_balance = new_balance + user_inputted_monthly_contr
    print("After month ",month," you would have $",round(new_balance,2),sep="") 
