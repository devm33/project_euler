
with open('p022_names.txt') as f:
    names = f.read().translate(None, '"').split(',')

base = ord('A') - 1

def score_word(word):
    score = 0
    for letter in word:
        score += ord(letter) - base
    return score

names.sort()

total = 0
for index, name in enumerate(names):
    total += score_word(name) * (index + 1)

print(total)