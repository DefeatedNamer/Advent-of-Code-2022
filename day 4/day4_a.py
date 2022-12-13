file = open("day 4\\input.txt", "r")
lines = file.read().split('\n') 

cumulative = 0

for line in lines:
    if not line:
        continue

    pair = line.split(',')
    limits = [list(map(int, pair[0].split('-'))), list(map(int, pair[1].split('-')))]

    if limits[0][0] <= limits[1][0] and limits[1][1] <= limits[0][1]:
        cumulative += 1

    elif limits[1][0] <= limits[0][0] and limits[0][1] <= limits[1][1]:
        cumulative += 1

print(cumulative)