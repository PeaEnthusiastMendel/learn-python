# Fibonacci Sequence to the nth term

n = int(input()) #number of terms
x = 0
y = 1
i = 3

print("1 :", x)
print("2 :", y)
while n >= i : # calculates to nth term
    z = x + y
    print(i, ":", z)
    x = y
    y = z
    i += 1

# needs better formatting - maybe turn into a list?