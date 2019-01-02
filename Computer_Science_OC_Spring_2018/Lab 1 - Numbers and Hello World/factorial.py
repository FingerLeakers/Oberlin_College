#Author: Trevor Martin
#Date of Completion: 17 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

factorial=1
n=int(input("Enter Integer:"))
for i in range(1,n+1):
    factorial = factorial*i
print("The factorial of the integer", n, "is", factorial)


