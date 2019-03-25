# Author: Trevor Martin
# Date of Completion: 6 March 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 4, primes.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Finds the first n primes
#===================================================================================================

def prime_classifier(number):
    
    # assume that the number is prime
    assume_prime = True
    # check if the number is prime
    for divisor in range(2, number):
        if number % divisor == 0:
            assume_prime = False
    # if the assumption was not found to be false
    if assume_prime == True:
        # we print the print and then return false
        print(number, end=" ", sep="")
        return True
    
    else:
        return False
                       
def main():
    # get user input 
    first_n_primes = int(input("Specify value for the first primes: "))
    prime_counter = 0
    number = 1
    previous_prime = -1
    number_of_twin_primes = 0
    
    print("The first ",first_n_primes," primes are:\n",sep="",end=" ")
    
    # keep looping until n primes
    while prime_counter < first_n_primes:
        # increases the number that you will check if it is a prime
        number += 1
        # classify the number as prime or not prime
        prime_number = prime_classifier(number)
        
        # if the number is a prime
        if prime_number:
            # increase the prime counter
            prime_counter += 1
            
            # if this prime number you found is next to another prime
            if number - previous_prime == 2:
                # it is a twin prime
                number_of_twin_primes += 1
            # make this number the previous prime
            previous_prime = number 
            
    print("\nAmongst these there are",number_of_twin_primes,"twin primes.")
    
main()





