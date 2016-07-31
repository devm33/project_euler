#!/usr/bin/env python2.7

# find n*n + a*n + b where |a| < 1000 and |b| < 1000

n = 10 ** 6

is_prime = [True] * n
is_prime[0] = False
is_prime[1] = False
for i in range(2, n):
    if is_prime[i]:
        for j in range(2 * i, n, i):
            is_prime[j] = False

def how_many_primes(a, b):
    n = 0
    cur = b
    while cur > 0 and is_prime[cur]:
        n += 1
        cur = n * n + a * n + b
    return n

result = (0, 0, 0)
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        cur = (how_many_primes(a, b), a, b)
        if result[0] < cur[0]:
            result = cur

print('%s primes with a=%s b=%s' % result)
