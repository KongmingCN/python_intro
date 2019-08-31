a = int(input())
b = int(input())

h1 = 1/(1/2 * (1/a + 1/b))

# calculate harmonic mean of a and b
h2 = 2 * a * b/(a + b)

print(h1, h2)