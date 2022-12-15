file = open("day 7\\input.txt", "r")
lines = file.read().split('\n')

dirs = None
file_sizes = {}

for line in lines:
    if not line:
        continue

    parts = line.split(' ')

    match parts:
        case ["$", "cd", "/"]:
            dirs = []

        case ["$", "cd", ".."]:
            dirs.pop(0)

        case ["$", "cd", *dir]:
            dirs.append(dir[0])

        case ["$", "ls"]:
            continue

        case ["dir", _]:
            continue

        case [*size]:
            for dir in dirs:
                file_sizes.setdefault(dir, 0)
                file_sizes[dir] += int(size[0])

cumulative = 0

for file, size in file_sizes.items():
    if size <= 100000:
        cumulative += size

print(cumulative)
