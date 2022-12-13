file = open("day 3\\input.txt", "r")
lines = file.read().split('\n') 

cumulative = 0

for idx in range(0, len(lines)-1, 3):
    bag1 = lines[idx]
    bag2 = lines[idx+1]
    bag3 = lines[idx+2]

    char = ''

    for idx in range(len(bag1)):
        if bag1[idx] in bag2 and bag1[idx] in bag3:
            char = bag1[idx]
            break
    
    if char.islower():
        cumulative += ord(char)-96
    else:
        cumulative += ord(char)-38

print(cumulative)