file = open("day 9\\input2.txt", "r")
lines = file.read().split('\n')

positions = {(0, 0)}

knots_coor = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


def move_knot(head, tail, write=False):
    if head[0] - tail[0] > 1:
        tail[0] += 1

        if head[1] - tail[1] == 1:
            tail[1] += 1

        elif head[1] - tail[1] == -1:
            tail[1] -= 1

        if write:
            positions.add(tuple(tail))

    elif head[0] - tail[0] < -1:
        tail[0] -= 1

        if head[1] - tail[1] == 1:
            tail[1] += 1

        elif head[1] - tail[1] == -1:
            tail[1] -= 1

        if write:
            positions.add(tuple(tail))

    elif head[1] - tail[1] > 1:
        tail[1] += 1

        if head[0] - tail[0] == 1:
            tail[0] += 1

        elif head[0] - tail[0] == -1:
            tail[0] -= 1

        if write:
            positions.add(tuple(tail))

    elif head[1] - tail[1] < -1:
        tail[1] -= 1

        if head[0] - tail[0] == 1:
            tail[0] += 1

        elif head[0] - tail[0] == -1:
            tail[0] -= 1

        if write:
            positions.add(tuple(tail))


def print_map():
    for y in range(-15, 15):
        for x in range(-15, 15):
            if [x, y] in knots_coor:
                print('X', end=" ")
            else:
                print('.', end=" ")

        print()

    input()


def print_positions():
    for y in range(20, -20, -1):
        for x in range(-20, 20):
            if (x, y) in positions:
                print('X', end=" ")
            else:
                print('.', end=" ")

        print()


def move(x, y, steps):
    # print_map()

    for _ in range(steps):
        knots_coor[0][0] += x
        knots_coor[0][1] += y

        for idx, knot in enumerate(knots_coor):
            if idx == len(knots_coor)-2:
                move_knot(knot, knots_coor[idx+1], True)
                break

            move_knot(knot, knots_coor[idx+1])


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

print(positions)
print(len(positions))
print_positions()
