file = open("day 2\\input.txt", "r")
lines = file.read().split('\n') 

lookup_table = {
    'A': 'R',
    'B': 'P',
    'C': 'S',

    'X': 'L',
    'Y': 'D',
    'Z': 'W'
}

shape_points = {
    'R': 1,
    'P': 2,
    'S': 3
}

round_points = {
    'L': 0,
    'D': 3,
    'W': 6
}

round_shape = {
    ('R', 'L'): 'S',
    ('R', 'D'): 'R',
    ('R', 'W'): 'P',
     
    ('P', 'L'): 'R',
    ('P', 'D'): 'P',
    ('P', 'W'): 'S',
     
    ('S', 'L'): 'P',
    ('S', 'D'): 'S',
    ('S', 'W'): 'R'
}

cumulative = 0

for line in lines:
    if not line:
        continue

    round = line.split(' ')
    processed_round = (lookup_table[round[0]], lookup_table[round[1]])

    print(processed_round)
    print(shape_points[round_shape[processed_round]])
    print(round_points[processed_round[1]])

    cumulative += shape_points[round_shape[processed_round]]
    cumulative += round_points[processed_round[1]]

print(cumulative)