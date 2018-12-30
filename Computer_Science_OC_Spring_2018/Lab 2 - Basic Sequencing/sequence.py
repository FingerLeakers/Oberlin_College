#sequence.py
#Program that lists the squares of all integers from some start number down to one
#Trevor Martin
#CSCI 150 20 February 2018
n=int(input("Enter Integer:"))
print("Squares from",n**2,"down to 1:")
for i in range(n, 0, -1):
    print(i**2," ",end="")


