#interest.py
#This program gets an initial deposit, a monthly interest rate, a monthly deposit, and a number of months n from the use, and provides the total money in possession at the end of n months.
#Trevor Martin
#CSCI 150 20 February 2018

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
    
