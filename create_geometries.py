import shapely
from shapely.geometry import Point, LineString, Polygon

#containers
points = []
lines = []


def createPointGeom(x_coord, y_coord):
    return Point(x_coord, y_coord)


def createLineGeom(list):
    pointsCnt = []
    for element in list:
        if type(element) is shapely.geometry.point.Point:
            pointsCnt.append(element)
        else:
            print(element, " is not Point type")
            continue
    return LineString(pointsCnt)


def createPolyGeom(coords):
    return Polygon(coords)


#demonstrate
point1 = createPointGeom(10.0, 20.0)
points.append(point1)

point2 = createPointGeom(20.0, 20.0)
points.append(point2)

point3 = createPointGeom(20.0, 10.0)
points.append(point3)

point4 = createPointGeom(10.0, 10.0)
points.append(point4)

print("p1:", point1 ,"p2:", point2,"p3:", point3,"p4:", point4)


line1 = createLineGeom(points)
print("line1:", line1)


listOfTuples = [(5.0, 10.0), (10.0, 10.0), (10.0, 5.0), (5.0, 5.0)]

polygon1 = createPolyGeom(listOfTuples)
print("polygon1:", polygon1)

polygon2 = createPolyGeom(points)
print("polygon2:", polygon2)


