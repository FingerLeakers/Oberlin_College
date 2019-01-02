#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

n=int(input("Enter Integer:"))

print("Squares from",n**2,"down to 1:")

for i in range(n, 0, -1):
    print(i**2," ",end="")


