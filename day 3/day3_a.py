file = open("day 3\\input.txt", "r")
lines = file.read().split('\n') 

cumulative = 0

for line in lines:
    if not line:
        continue

    length = len(line)
    split_idx = int(length/2)
    
    compartment1 = line[:split_idx]
    compartment2 = line[split_idx:]

    char = ''

    for idx in range(split_idx):
        if compartment1[idx] in compartment2:
            char = compartment1[idx]
            break
    
    if char.islower():
        cumulative += ord(char)-96
    else:
        cumulative += ord(char)-38

print(cumulative)