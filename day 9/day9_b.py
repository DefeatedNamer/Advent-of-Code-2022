file = open("day 9\\input2.txt", "r")
lines = file.read().split('\n')

positions = {(0, 0)}

head_coor = [0, 0]
knots_coor = [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


def move_tail(head, tail):
    if head[0] - tail[0] > 1:
        tail[0] += 1

        if head[1] - tail[1] == 1:
            tail[1] += 1

        elif head[1] - tail[1] == -1:
            tail[1] -= 1

        positions.add(tuple(tail))

    elif head[0] - tail[0] < -1:
        tail[0] -= 1

        if head[1] - tail[1] == 1:
            tail[1] += 1

        elif head[1] - tail[1] == -1:
            tail[1] -= 1

        positions.add(tuple(tail))

    elif head[1] - tail[1] > 1:
        tail[1] += 1

        if head[0] - tail[0] == 1:
            tail[0] += 1

        elif head[0] - tail[0] == -1:
            tail[0] -= 1

        positions.add(tuple(tail))

    elif head_coor[1] - tail[1] < -1:
        tail[1] -= 1

        if head_coor[0] - tail[0] == 1:
            tail[0] += 1

        elif head_coor[0] - tail[0] == -1:
            tail[0] -= 1

        positions.add(tuple(tail))


def move_head(x, y, steps):
    for _ in range(steps):
        head_coor[0] += x
        head_coor[1] += y

        print(positions)
        print(len(positions))
        input()

        for idx, knots in enumerate(knots_coor):
            if idx == 0:
                move_tail(head_coor, knots_coor[idx])

            if idx == len(knots)-1:
                break

            move_tail(knots_coor[idx], knots_coor[idx+1])


for line in lines:
    if not line:
        continue

    match line.split(' '):
        case ['R', *steps]:
            steps = int(steps[0])
            move_head(+1, 0, steps)

        case ['D', *steps]:
            steps = int(steps[0])
            move_head(0, -1, steps)

        case ['L', *steps]:
            steps = int(steps[0])
            move_head(-1, 0, steps)

        case ['U', *steps]:
            steps = int(steps[0])
            move_head(0, +1, steps)
