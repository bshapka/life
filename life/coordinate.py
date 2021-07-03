from typing import NamedTuple

"""
represents an ordered pair in the xy plane

fields:
    x: int
        represents the x-coordinate in the ordered pair
        
    y: int
        represents the y-coordinate in the ordered pair
"""
Coordinate = NamedTuple("Coordinate", [("x", int), ("y", int)])
