file = open("day 6\\input.txt", "r")
lines = file.read().split('\n')

n_chars = 14
current_chars = []
indexes = []

for idx, char in enumerate(lines[0]):
    if idx < n_chars:
        current_chars.append(char)
        continue

    else:
        current_chars.pop(0)
        current_chars.append(char)

    unique_chars = set(current_chars)

    if len(unique_chars) == n_chars:
        indexes.append(idx+1)

print(indexes[0])
