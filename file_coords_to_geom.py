import pandas as pd
from shapely.geometry import Point

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
