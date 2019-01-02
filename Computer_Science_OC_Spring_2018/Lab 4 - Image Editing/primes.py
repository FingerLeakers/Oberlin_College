#Author: Trevor Martin
#Date of Completion: 6 March 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Easy

#This function prints x if x is a prime number.
def isPrime(x):
    
    assumePrime = True
    for div in range(2, x):
        
        if x%div==0:
            assumePrime = False
            
    if assumePrime == True:
        print(x)
        return True
    
    else:
        return False
           
#This function calls all other functions.            
def main():
    
    limit=int(input("Specify value n:"))
    count=0
    num=1
    OldPrime=-1
    TwinPrimes=0
    
    print("The first",limit,"primes are:\n",sep=" ",end=" ")
    
    while count < limit:
        num=num+1
        isAPrime = isPrime(num)
        
        if isAPrime:
            count=count+1
            
            if num-OldPrime==2:
                TwinPrimes=TwinPrimes+1
            OldPrime=num
            
    print("Amongst these there are",TwinPrimes,"twin primes")
    
main()





