# nth term of the Fibonacci Sequence

print("Which term are you seeking?")
n = int(input()) # the term you want
x = 0
y = 1
i = 3

while i <= n : # iterates through Fibonacci Sequence
    z = x + y
    x = y
    y = z
    i += 1
    if i == n+1: # "Are we there yet?"
        print("Term", n, "of the Fibonacci Sequence is", z)
        break