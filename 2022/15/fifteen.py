# we have pairings of sensors and beacons. Sensors know the location of the closest beacon. Because it's the 'closest' we know no position inside the same radius is a beacon. Since we know this, we can mark the radius around each sensor as unable to contain a beacon. Then we can do this for every sensor, then check the target line and see how many spots are taken up by marks.

#Okay I solved pt 1 by just checking which sets of deltas between sensor coords and their respective beacons added and minused to their sensor's y coordinate would cross the chosen y_line, then calculated the spread of non-beacon area based on how far across past the y_line the delta reached. So not brute force.

#Part two I'm having trouble understanding exactly what they're asking for. Okay so it seems like they're asking for a singular position that will be open when you run this algorithm across a space of 4,000,000 square spaces, starting from 0 for both x and y values. I may have to optimize.

from re import findall

i_n, useful, y_line, not_beacons, offset, total = list(list(map(int, findall(r"-?\d+", l))) for l in open('2022/15/input.txt').read().splitlines()), [], 10, ['_' for _ in range(30)], 0, 0



for coords in i_n:
    delta = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
    if (y_line - coords[1] >= 0 and coords[1] + delta >= y_line) or (y_line - coords[1] < 0 and coords[1] - delta <= y_line):
        useful.append(((coords[0], coords[1]), delta))
    if coords[3] == y_line:
        not_beacons[coords[2] + offset] = 'O'

print(useful)


for coords, delta in useful:
    if y_line - coords[1] > 0:
        coverage = (coords[1] + delta) - y_line
    elif y_line - coords[1] < 0:
        coverage = y_line - (coords[1] - delta)
    else:
        not_beacons[coords[0] + offset] = 'O'
        coverage = delta
    for pos in range(0, coverage + 1):
        not_beacons[coords[0] + pos + offset] = '#' if not_beacons[coords[0] + pos + offset] != 'O' else 'O'
    for neg in range(0, -coverage - 1, -1):
        not_beacons[coords[0] + neg + offset] = '#' if not_beacons[coords[0] + neg + offset] != 'O' else 'O'
    
for item in not_beacons:
    if item == '#':
        total += 1

# print(not_beacons)
print(total)
    

