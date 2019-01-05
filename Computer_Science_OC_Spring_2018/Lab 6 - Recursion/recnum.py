#Author: Trevor Martin
#Date of Completion: 28 March 2018
#Data of Edits: 5 January 2019
#Language: Python 3
#Difficulty: Easy

def main():
    n=int(input("Please provide a positive integer n:"))
    k=int(input("Please provide a second positive integer k:"))
    print(n, "raised to the power of", k, "is",Powers(n,k))
    print("The sum of the first",n,"squares is",SumOfSquares(n,k))
    print(n,"choose",k,"is",Choose(n,k))
    
#Computes n raised to the power of k   
def Powers(n,k):
    if k==0:
        return 1
    return n * Powers(n,k-1)

#Computes the sum of the first n perfect squares
def SumOfSquares(n,k):

    if n**2==1:
        return 1
    return n**2 + SumOfSquares(n-1, k)

        
#Choose possible combinations (k) from a set of objects (n)
def Choose(n,k):
   
    if k==0 or k==n:
        return 1
    elif k>n:
        return 0
    return Choose(n-1,k) + Choose(n-1, k-1)
    
        
main()
