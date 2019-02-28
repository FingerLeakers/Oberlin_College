#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

n=eval(input("Enter Input:"))
for row in range(1, n+2):
    for col in range(1,row):
        for num in range(0, col):
            print(col, end=" ")
    print()
