#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

# print("Trevor's Fibonacci Number Generator")
# while True:
#     n=int(input("Enter Positive Integer Please:"))
#     if n > 2:
#         break
#     else:
#         print("Please enter a number larger than 2.")
# current=1
# previous=1
# for i in range(0,n-2):
#     store = current
#     current=current+previous
#     previous = store
# print("The ", n,"th number in the Fibonacci sequence is ", current, sep="")

start = int(input("Please pick an integer greater than 2."))
previous = 1
current = 1

for i in range(start-2):
    current = (current + previous)
    previous = (current - previous)
    
print("The", start, "number in the Fibonacci Sequence is:", current)


