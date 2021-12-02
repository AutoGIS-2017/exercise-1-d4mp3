import create_geometries as ex1
import shapely

def getCentroid(obj):
    return obj.centroid


def getArea(obj):
    return obj.area


def getLength(obj):
    if type(obj) is shapely.geometry.linestring.LineString or type(obj) is shapely.geometry.polygon.Polygon:
        return obj.length
    else:
        print("Error: LineString or Polygon geometries required!")
        return 0


#demonstrate
centr1 = getCentroid(ex1.polygon1)
print("centroid of polygon1(", ex1.polygon1, ") is:", centr1)

centr2 = getCentroid(ex1.line1)
print("centroid of line1 (", ex1.line1, ") is:", centr2)


area1 = getArea(ex1.polygon1)
print("area of polygon1(", ex1.polygon1, ") is:", area1)

len1 = getLength(ex1.polygon1)
print("length of polygon1 is", len1)

len2 = getLength(ex1.line1)
print("length of line1 is", len2)