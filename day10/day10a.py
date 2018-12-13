# First program to find the iteration with the minimal spread of points
# I assumed that this would be the one that displayed the message.
# Initial try of 10100 found through trial and error.
# The output tells us that the minimal spread is for iteration 10117.
# This made Part 2 trivial.
import re
a = [[int(n) for n in re.findall('[-0-9]+', x)] for x in open('day10').readlines()]
for x in a:
    x[0] += 10100 * x[2]
    x[1] += 10100 * x[3]

for i in range(100):
    width = max((x[0] for x in a)) - min((x[0] for x in a))
    height = max((x[1] for x in a)) - min((x[1] for x in a))
    print(i,width,height)
    for x in a:
        x[0] += x[2]
        x[1] += x[3]
