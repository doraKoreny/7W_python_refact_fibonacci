i, j, k, fib = 0, 1, 0, 0
print("The first 30 numbers of the Fibonacci sequences are these: ")
i = 1
while i <= 30:
    print(fib)
    fib = j + k
    j = k
    k = fib
    i = i + 1
else:
    print("Finished!")
