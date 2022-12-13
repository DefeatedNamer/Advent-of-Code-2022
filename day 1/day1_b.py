file = open("day 1\\input.txt", "r")
lines = file.read().split('\n') 

top1 = 0
top2 = 0
top3 = 0
cumulative = 0

for line in lines:
    if line:
        cumulative += int(line)

    else: 
        if cumulative > top1:
            top3 = top2
            top2 = top1
            top1 = cumulative
        elif cumulative > top2:
            top3 = top2
            top2 = cumulative
        elif cumulative > top3:
            top3 = cumulative

        cumulative = 0

print(top1 + top2 + top3)