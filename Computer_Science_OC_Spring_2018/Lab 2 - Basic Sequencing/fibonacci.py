#     
print("Trevor's Fibonacci Number Generator")
while True:
    n=int(input("Enter Positive Integer Please:"))
    if n > 2:
        break
    else:
        print("Please enter a number larger than 2.")
current=1
previous=1
for i in range(0,n-2):
    store = current
    current=current+previous
    previous = store
print("The ", n,"th number in the Fibonacci sequence is ", current, sep="")



