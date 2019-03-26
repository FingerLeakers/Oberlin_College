# Author: Trevor Martin
# Date of Completion: 28 March 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 6, recnum.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program uses recursion to raise numbers to a user input power and find the sum of squares
# It also does a binomial procedure of "n binomial k"
#===================================================================================================

def main():
    first_input =int(input("Please provide a positive integer: "))
    second_input =int(input("Please provide a second positive integer: "))
    print(first_input,"raised to the power of",second_input,"is",exponential(first_input,second_input))
    print("The sum of the first",n,"squares is",find_sum_of_squares(first_input,second_input))
    print(first_input,"choose",second_input,"is",binomial(first_input,second_input))
    
#Computes n raised to the power of k   
def exponential(n,k):
    if k==0:
        return 1
    return n * exponential(n,k-1)

#Computes the sum of the first n perfect squares
def find_sum_of_squares(n,k):

    if n**2==1:
        return 1
    return n**2 + find_sum_of_squares(n-1, k)

        
#binomial possible combinations (k) from a set of objects (n)
def binomial(n,k):
   
    if k==0 or k==n:
        return 1
    elif k>n:
        return 0
    return binomial(n-1,k) + binomial(n-1, k-1)
    
        
main()
