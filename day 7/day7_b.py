file = open("day 7\\input.txt", "r")
lines = file.read().split('\n')

dirs = []
dir_sizes = {}

for line in lines:
    if not line:
        continue

    parts = line.split(' ')

    match parts:
        case ["$", "cd", ".."]:
            dirs.pop(-1)

        case ["$", "cd", dir]:
            dir_name = dir
            count = 0

            while dir_name in dir_sizes:
                count += 1
                dir_name = dir + str(count)

            dirs.append(dir_name)
            dir_sizes[dir_name] = 0

        case ["$", "ls"]:
            continue

        case ["dir", _]:
            continue

        case [*parts]:
            for dir in dirs:
                dir_sizes[dir] += int(parts[0])

total_space = 70000000
needed_space = 30000000

used_space = dir_sizes['/']
free_space = total_space - used_space
need_to_free = needed_space - free_space

answer = total_space

for dir, parts in dir_sizes.items():
    if parts >= need_to_free:
        answer = min(answer, parts)

print(answer)
