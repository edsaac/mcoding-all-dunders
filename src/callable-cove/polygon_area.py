from itertools import starmap
from operator import mul


def polygon_area(
    vertices: list[tuple[float, float]], *, scale: float = 1.0
) -> float:
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

    return area * scale**2


def batch_areas(*polygons):
    return [polygon_area(p) for p in polygons]


def main():
    square = [(0, 0), (2, 0), (2, 2), (0, 2)]
    triangle = [(0, 0), (1, 0), (0, 1)]
    octagon = [
        ( 0.414, 1.000),
        ( 1.000, 0.414),
        ( 1.000, -0.414),
        ( 0.414, -1.000),
        (-0.414, -1.000),
        (-1.000, -0.414),
        (-1.000, 0.414),
        (-0.414, 1.000)
    ]

    print(f"{polygon_area(square) = }")
    print(f"{polygon_area(triangle) = }")
    print(f"{polygon_area(octagon) = }")

    print(f"{polygon_area(square, scale=0.5) = }")

    print(polygon_area.__defaults__)
    print(polygon_area.__kwdefaults__)

    print(
        """
        Turns out the coordinates are in m but we needed
        the areas in ft²  
        """
    )


if __name__ == "__main__":
    main()
