
def next(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1

def len_sequence(n):
    count = 0
    while n != 1:
        n = next(n)
        count += 1
    return count

number = 0
length = 0

for n in range(10 ** 6, 0, -1):
    cur = len_sequence(n)
    if cur > length:
        length = cur
        number  = n

print(number, length)