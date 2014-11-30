from math import sqrt

def proper_divisors(n):
    output = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            output.append(i)
            if i != n/i and i != 1:
                output.append(n/i)
    return output

def sum_divisors(n):
    return sum(proper_divisors(n))

def has_sum(n, sum_list, sum_map):
    for s in sum_list:
        if s > n/2 + 1:
            return False
        if sum_map[n - s]:
            return True
    return False

UPPER = 28123 + 1000

is_abundant = [False] * UPPER
abundant = []
nonabunsum = []
for n in range(1, UPPER):
    if sum_divisors(n) > n:
        abundant.append(n)
        is_abundant[n] = True

for n in range(1, UPPER):
    if not has_sum(n, abundant, is_abundant):
        nonabunsum.append(n)

print(abundant)
print(nonabunsum)
print(sum(nonabunsum))