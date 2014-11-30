
def proper_divisors(n):
    for i in range(1, n):
        if n % i == 0:
            yield i

divisor_sums = [0, 0, 1]
amicable_numbers = []

for n in range(3, 10000):
    sum_proper_divisors = sum(list(proper_divisors(n)))
    divisor_sums.append(sum_proper_divisors)
    if sum_proper_divisors < n:
        if divisor_sums[sum_proper_divisors] == n:
            amicable_numbers.append(n)
            amicable_numbers.append(sum_proper_divisors)

print(sum(amicable_numbers))