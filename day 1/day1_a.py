file = open("day 1\\input.txt", "r")
lines = file.read().split('\n') 

max = 0
cumulative = 0

for line in lines:
    if line:
        cumulative += int(line)

    else: 
        if cumulative > max:
            max = cumulative
        cumulative = 0


print(max)
