
N = 2 * 10 ** 6

is_prime = [True] * N
primes = []

for n in range(2, N):
    if is_prime[n]:
        primes.append(n)
        for m in range(2 * n, N, n):
            is_prime[m] = False


print(primes)
print(sum(primes))