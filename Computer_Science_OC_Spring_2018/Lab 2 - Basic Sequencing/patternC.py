#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

user_input = int(input("Enter Input: "))
for row in range(1, user_input+1):
    for column in range(row, n+1):
        print(column, end=" ")    
    print()
