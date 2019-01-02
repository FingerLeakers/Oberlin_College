#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

n=eval(input("Enter # of Months:"))
IS=eval(input("Enter your initial savings:"))
I=eval(input("Enter the monthly interest:"))
u=eval(input("Enter your monthly contribution:"))
total = IS
print("Initially you put in %d."%IS)
for i in range(1,n+1):
    interest = total*I
    total = total + interest
    total = total + u
    print("After month %d you would have $%.2f."%(i,total))
    
