from itertools import starmap
from operator import mul


def polygon_area(vertices: list[tuple[float, float]]) -> float:
    """Calculate the area of a polygon from a list of
    coordinates x,y using the Gauss's (shoelace) formula.

    """
    if len(vertices) > 1:
        xcoord, ycoord = zip(*vertices)
        xstepd = [xcoord[-1], *xcoord[:-1]]
        ystepd = [ycoord[-1], *ycoord[:-1]]

        slash = sum(starmap(mul, zip(xcoord, ystepd)))
        back = sum(starmap(mul, zip(ycoord, xstepd)))

        area = 0.5 * (back - slash)

    else:
        area = 0.0

    return area


print(f"{polygon_area([(0,0), (2,0), (2,2), (0,2)]) = }")
print(f"{polygon_area([(0,0), (1,0), (0,1)]) = }")
