from __future__ import annotations

"""Challenge Question."""

__author__ = "730664108"


class Point:
    """Point class."""

    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mulltiplies x * factor and y * factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns a new point."""
        new_point_x = self.x * factor
        new_point_y = self.y * factor
        return Point(new_point_x, new_point_y)
    
    def __str__(self):
        """Print prettier version of our point."""
        return f"({self.x},{self.y})"
    
    def __mul__(self, factor: float) -> Point:
        """Returns a new point."""
        new_point_x = self.x * factor
        new_point_y = self.y * factor
        return Point(new_point_x, new_point_y)
    
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            IndexError



a: Point = Point (1.0, 2.0)
b: Point = a * 3.0
# can call mul by *
print(b[0]) #y-coord