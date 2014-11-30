
under20 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def word(n):
    if n == 100:
        return 'onehundred'
    if n == 1000:
        return 'onethousand'

    cur = ''
    if n % 100 < 20:
        if n % 20 != 0:
            cur = under20[n % 20 - 1]
    else:
        if n % 10 != 0:
            cur = under20[n % 10 - 1]
        cur = tens[(n % 100)/10 - 2] + cur

    if n > 100:
        if len(cur) > 0:
            cur = 'and' + cur
        cur = 'hundred' + cur
        cur  = under20[n/100 - 1] + cur

    return cur

s = ''
for n in range(1, 1001):
    print('%4d %s' % (n, word(n)))
    s = word(n) + s
print(len(s))