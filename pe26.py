from math import log10, ceil, floor

def length_of_repeating_decimal(n):
    visited = {}
    order = int(ceil(log10(n)))
    cur = 10 ** order
    length = 0
    while cur not in visited:
        visited[cur] = True
        length += 1
        cur = cur - (n * floor(cur / n))
        if cur == 0:
            return 0
        cur = cur * (10 ** (1 + order - int(ceil(log10(cur)))))
    return length


result = (0, 0)
for n in range(2, 1000):
    cur = (length_of_repeating_decimal(n), n)
    if cur > result:
        print(cur)
        result = cur

print('length: %s denom: %s' % result)