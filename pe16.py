
# e = 2 ** 1000
# the nth digit of e is pow(2, 1000, 10 ** n) / (10 ** (n-1))
# the number of digits of e is  ceiling of math.log(e, 10) = 301.02...

from math import log, ceil
e = 2 ** 1000
N = int(ceil(log(e, 10)))
print(e)
s = 0
for n in range(1, N + 1):
    print((e % (10 ** n)) / (10 ** (n-1)))
    s += (e % (10 ** n)) / (10 ** (n-1))

print(s)