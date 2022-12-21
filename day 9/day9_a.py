file = open("day 9\\input.txt", "r")
lines = file.read().split('\n')

positions = {(0, 0)}

head_coor = [0, 0]
tail_coor = [0, 0]


def move(x, y, steps):
    for _ in range(steps):
        head_coor[0] += x
        head_coor[1] += y

        if head_coor[0] - tail_coor[0] > 1:
            tail_coor[0] += 1

            if head_coor[1] - tail_coor[1] == 1:
                tail_coor[1] += 1

            elif head_coor[1] - tail_coor[1] == -1:
                tail_coor[1] -= 1

            positions.add(tuple(tail_coor))

        elif head_coor[0] - tail_coor[0] < -1:
            tail_coor[0] -= 1

            if head_coor[1] - tail_coor[1] == 1:
                tail_coor[1] += 1

            elif head_coor[1] - tail_coor[1] == -1:
                tail_coor[1] -= 1

            positions.add(tuple(tail_coor))

        elif head_coor[1] - tail_coor[1] > 1:
            tail_coor[1] += 1

            if head_coor[0] - tail_coor[0] == 1:
                tail_coor[0] += 1

            elif head_coor[0] - tail_coor[0] == -1:
                tail_coor[0] -= 1

            positions.add(tuple(tail_coor))

        elif head_coor[1] - tail_coor[1] < -1:
            tail_coor[1] -= 1

            if head_coor[0] - tail_coor[0] == 1:
                tail_coor[0] += 1

            elif head_coor[0] - tail_coor[0] == -1:
                tail_coor[0] -= 1

            positions.add(tuple(tail_coor))


for line in lines:
    if not line:
        continue

    match line.split(' '):
        case ['R', steps]:
            steps = int(steps)
            move(+1, 0, steps)

        case ['D', steps]:
            steps = int(steps)
            move(0, -1, steps)

        case ['L', steps]:
            steps = int(steps)
            move(-1, 0, steps)

        case ['U', steps]:
            steps = int(steps)
            move(0, +1, steps)

print(len(positions))
