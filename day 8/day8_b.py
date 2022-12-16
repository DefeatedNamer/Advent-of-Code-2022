file = open("day 8\\input.txt", "r")
lines = file.read().split('\n')

tree_2d_array = []
scenic_scores = []

height = 0
width = 0

for y, line in enumerate(lines):
    if not line:
        continue

    tree_2d_array.append([])
    height += 1

    for x, tree in enumerate(line):
        tree_2d_array[y].append(int(tree))

width = len(tree_2d_array[0])


def get_scenic_score(x, y):
    tree = tree_2d_array[y][x]

    east = 0
    west = 0
    south = 0
    north = 0

    for n in range(x+1, width):
        east += 1
        if tree_2d_array[y][n] >= tree:
            break

    for n in range(x-1, -1, -1):
        west += 1
        if tree_2d_array[y][n] >= tree:
            break

    for n in range(y+1, height):
        south += 1
        if tree_2d_array[n][x] >= tree:
            break

    for n in range(y-1, -1, -1):
        north += 1
        if tree_2d_array[n][x] >= tree:
            break

    return east * west * south * north


for y in range(height):
    for x in range(width):
        scenic_scores.append(get_scenic_score(x, y))

print(max(scenic_scores))
