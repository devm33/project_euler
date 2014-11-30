
# max path sum I
rows = []

# filename = 'pe18.txt'
filename = 'p067_triangle.txt'

with open(filename) as f:
    for line in f:
        rows.append(line.split(' '))

for i, row in enumerate(rows):
    rows[i] = map(int, row)

print(rows)

for row in range(len(rows) - 2, -1, -1):
    for pos in range(0, len(rows[row])):
        rows[row][pos] = rows[row][pos] + max(rows[row + 1][pos], rows[row + 1][pos + 1])

print(rows)