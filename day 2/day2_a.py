file = open("day 2\\input.txt", "r")
lines = file.read().split('\n') 

lookup_table = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

shape_points = {
    'R': 1,
    'P': 2,
    'S': 3
}

round_points = {
    ('R', 'R'): 3,
    ('R', 'P'): 6,
    ('R', 'S'): 0,
     
    ('P', 'R'): 0,
    ('P', 'P'): 3,
    ('P', 'S'): 6,
     
    ('S', 'R'): 6,
    ('S', 'P'): 0,
    ('S', 'S'): 3
}

cumulative = 0

for line in lines:
    if not line:
        continue

    round = line.split(' ')
    processed_round = (lookup_table[round[0]], lookup_table[round[1]])

    cumulative += shape_points[processed_round[1]]
    cumulative += round_points[processed_round]

print(cumulative)
        
