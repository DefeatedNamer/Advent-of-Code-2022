file = open("day 5\\input.txt", "r")
lines = file.read().split('\n') 

cumulative = 0

stack1 = ['P', 'G', 'R', 'N']
stack2 = ['C', 'D', 'G', 'F', 'L', 'B', 'T', 'J']
stack3 = ['V', 'S', 'M']
stack4 = ['P', 'Z', 'C', 'R', 'S', 'L']
stack5 = ['Q', 'D', 'W', 'C', 'V', 'L', 'S', 'P']
stack6 = ['S', 'M', 'D', 'W', 'N', 'T', 'C']
stack7 = ['P', 'W', 'G', 'D', 'H']
stack8 = ['V', 'M', 'C', 'S', 'H', 'P', 'L', 'Z']
stack9 = ['Z', 'G', 'W', 'L', 'F', 'P', 'R']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

#     [C]         [Q]         [V]    
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]
#  1   2   3   4   5   6   7   8   9 

for idx, line in enumerate(lines):
    if idx < 10:
        continue

    if not line:
        continue

    elements = line.split(' ')
    n_boxes = int(elements[1])
    from_stack = int(elements[3]) - 1
    to_stack = int(elements[5]) - 1

    for n in range(n_boxes):
        stacks[to_stack].insert(n, stacks[from_stack][n])
        
    for n in range(n_boxes):
        stacks[from_stack].pop(0)


for stack in stacks:
    print(stack[0])
