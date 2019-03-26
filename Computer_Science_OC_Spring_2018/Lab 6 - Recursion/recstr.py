# Author: Trevor Martin
# Date of Completion: 28 March 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 6, recstr.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program recursively checks whether or not a string is determine_palindrome and whether or not a
# second string is a subsequence of the first string
#===================================================================================================

def main():
    first_string = str(input("Please provide a first_string:"))
    second_string = str(input("Please provide a second_string:"))
    print("The string ",first_string," backwards is ",reverse(first_string),".",sep="") 
    if determine_palindrome(first_string) == True:
        print("The string",first_string,"is a determine_palindrome.")
    elif determine_palindrome(first_string) == False:
        print("The string",first_string,"is not a determine_palindrome.")
    if determine_subsequence(first_string, second_string) == True:
        print(second_string,"is a sequence of",first_string)
    elif determine_subsequence(first_string,second_string) == False:
        print(second_string,"is not a sequence of",first_string)
   
# this function takes a string and reverses the order of its letters.
def reverse(user_input):
    if len(user_input) == 0:
        # base case for a string is "" 
        return ""
    elif len(user_input) > 0:
        last_letter = user_input[-1]
        return last_letter + reverse(user_input[:-1])
                     
# this function finds if a string is read the same forwards as reversed.
# user input here is some string
def determine_palindrome(user_input):
    if len(user_input)==0 or len(user_input)==1:
        return True
    elif user_input[0] == user_input[-1] and determine_palindrome(user_input[1:-1]):
        return True
    else:
        return False

# this finds whether or not second_string is a sequence of first_string.
def determine_subsequence(first_string, second_string):
    if len(second_string)==0:
        return True
    elif len(second_string) > len(first_string):
        return False
    elif first_string[0] == second_string[0] and determine_subsequence(first_string[1:], second_string[1:]):
        return True
    elif first_string[0] != second_string[0] and determine_subsequence(first_string[1:], second_string[1:]):
        return False
    
main()
