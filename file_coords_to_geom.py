import pandas as pd
from shapely.geometry import Point, LineString

orig_points = []
dest_points = []


df = pd.read_csv('travelTimes_2015_Helsinki.txt', sep = ';')

from_x = df.from_x
from_y = df.from_y

to_x = df.to_x
to_y = df.to_y

#iterate over orgi
for (x,y) in zip(from_x,from_y):
    orig_points.append(Point(x, y))


#iterate over dest
for (x,y) in zip(to_x,to_y):
    dest_points.append(Point(x, y))

#Problem 4 SOLUTION


lines = []
lines2 = []

for (p1, p2) in zip(orig_points, dest_points):
    lines.append(LineString([p1, p2]))


def avgDist(arg1, arg2):
    b = 0
    for (arg1, arg2) in zip(arg1, arg2):
        lines2.append(LineString([arg1, arg2]))

    for line in lines2:
        b = b + line.length
    return b / len(lines2)

