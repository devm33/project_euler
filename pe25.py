
# fibonacci series first 1000 digit number

n0 = 1
n1 = 1
count = 2
stop = 10 ** 999 - 1

while True:
    n2 = n0 + n1
    n0 = n1
    n1 = n2
    count += 1
    if n1 > stop:
        print(n0)
        print(len(str(n0)))
        print(n1)
        print(len(str(n1)))
        print(count)
        exit()