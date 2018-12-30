print("Pattern N Generator:")
n=int(input("Enter the index(must be greater than 2):"))
if n<2:
    print("Please enter an integer 2 or greater")
else:
    print("*", end="")
    for i in range(1, n+1):
        print(" ", end="")
    print("*", end="")
    print()

    for i in range(1, n+1):
        print("*", end="")
        for j in range(1, n+1):
            if j==i:
                print("*", end="")
            else:
                print(" ", end="")
        print("*", end="")
        print()
                
    print("*", end="")
    for i in range(1, n+1):
        print(" ", end="")
    print("*", end=" ")
    print()
