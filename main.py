def myfunction(n):
    for i in range(0, n + 1):  # Outer loop runs n + 1 times
        print("First loop")
        j = 1
        while j <= n + 1:      # Inner while loop
            print("Second loop", j)
            j = j * 2          # j is multiplied by 2 in each iteration
    for i in range(0, 100):   # This loop runs a constant 100 times
        print("Third loop")