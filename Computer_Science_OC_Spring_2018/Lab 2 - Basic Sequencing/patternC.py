n=eval(input("Enter Input:"))
for row in range(1, n+1):
    for col in range(row, n+1):
        print(col, end=" ")    
    print()
