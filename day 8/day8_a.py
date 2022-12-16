file = open("day 8\\input.txt", "r")
lines = file.read().split('\n')

tree_2d_array = []
visible_checklist = {}

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

for y in range(height):
    max = -1

    for x in range(width):
        tree = tree_2d_array[y][x]

        if tree > max:
            max = tree
            visible_checklist[(x, y)] = True
        else:
            visible_checklist[(x, y)] = False

    max = -1

    for x in range(width-1, -1, -1):
        tree = tree_2d_array[y][x]

        if tree > max:
            max = tree
            visible_checklist[(x, y)] = True


for x in range(width):
    max = -1

    for y in range(height):
        tree = tree_2d_array[y][x]

        if tree > max:
            max = tree
            visible_checklist[(x, y)] = True

    max = -1

    for y in range(height-1, -1, -1):
        tree = tree_2d_array[y][x]

        if tree > max:
            max = tree
            visible_checklist[(x, y)] = True

cumulative = 0

for visible in visible_checklist.values():
    if not visible:
        cumulative += 1

print(cumulative)
