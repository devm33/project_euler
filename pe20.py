
def sum_digits(n):
    total = 0
    while n > 10:
        total += n % 10
        n = n / 10
    return total + n


from math import factorial

print (sum_digits(factorial(100)))