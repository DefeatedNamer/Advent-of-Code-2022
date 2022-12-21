file = open("day 10\\input2.txt", "r")
lines = file.read().split('\n')


X = 1
cycles = 0
cumulative = 0


for line in lines:
    if not line:
        continue

    match line.split(' '):
        case ['noop']:
            cycles += 1
            if cycles % 20 == 0:
                cumulative += cycles*X

        case ['addx', n]:
            cycles += 1
            if cycles % 20 == 0:
                cumulative += cycles*X
            cycles += 1
            if cycles % 20 == 0:
                cumulative += cycles*X

            X += int(n)

print(cumulative)
