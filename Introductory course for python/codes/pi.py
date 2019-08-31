d = int(input())

#Challenge: change this to f-string
print('+'+'-'*d+'+--------+')

n_str = 'n'
print(f'|{n_str:^{d}}|   pi   |')
print('+'+'-'*d+'+--------+')

for i in range(d):
    n = 10**i
    pi = 0
    for i in range(n):
        pi += (-1) ** i * 4 / (2 * i + 1)

    print(f'|{n:{d}d}|{pi:f}|')

print('+'+'-'*d+'+--------+')
