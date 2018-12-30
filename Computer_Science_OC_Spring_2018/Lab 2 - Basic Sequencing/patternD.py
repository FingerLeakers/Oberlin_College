n=eval(input("Enter Input:"))
for row in range(1, n+2):
    for col in range(1,row):
        for num in range(0, col):
            print(col, end=" ")
    print()       
    

