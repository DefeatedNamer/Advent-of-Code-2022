file = open("day 7\\input.txt", "r")
lines = file.read().split('\n')

dirs = None
dir_sizes = {}

for line in lines:  
    if not line:
        continue

    parts = line.split(' ')

    match parts:
        case ["$", "cd", "/"]:
            dirs = []

        case ["$", "cd", ".."]:
            dirs.pop(-1)

        case ["$", "cd", *dir]:
            dir = dir[0]
            count = 0

            while dir in dir_sizes:
                count += 1
                dir = dir[0] + str(count)
            
            dirs.append(dir)
            dir_sizes[dir] = 0

        case ["$", "ls"]:
            continue

        case ["dir", _]:
            continue

        case [*size]:
            for dir in dirs:
                dir_sizes[dir] += int(size[0])

cumulative = 0

for dir, size in dir_sizes.items():
    if size <= 100000:
        cumulative += size

print(cumulative)
