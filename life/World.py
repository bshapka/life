import collections
import functools
import operator
from typing import List, Set
from life.Coordinate import Coordinate

class World:
    """
    represents a 2D world in grid form with each cell in the grid being live or dead (but not both)

    fields:
        state: Set[Coordinate]
            represents the state of the world as a set of 2-integer tuples. Each element of the set
            gives the coordinates of a live cell in the grid. As such, the coordinates of dead cells
            are not part of the state.

    methods:
        next_state() -> None
            updates state by applying the rules of the game

        state() -> Set[Coordinate]
            returns state
    """

    def __init__(self, initial_state: Set[Coordinate]) -> None:
        """
        instantiates a World

        :param initial_state: an initial state of the World

        :returns None
        """
        World.__validate_state(initial_state)
        self.__state = initial_state

    @staticmethod
    def __validate_state(state: Set[Coordinate]) -> None:
        """
        validates a given state

        checks that state is of type Set[Coordinate]

        :raises TypeError if state is not of type Set

        :raises TypeError if any element of state is not of type Coordinate

        :raises TypeError if any element of any element of state is not not of type int

        :param state: a state for the World

        :returns None
        """
        error_message = "The state must be of type Set[Coordinate]. "

        if type(state) is not set:
            error_message += "The collection used is not of type set."
            raise TypeError(error_message)

        for coordinate in state:
            if type(coordinate) is not Coordinate:
                error_message += "An element of the set is not a Coordinate."
                raise TypeError(error_message)
            for component in coordinate:
                if type(component) is not int:
                    error_message += "A Coordinate in the set contains an element that is not of type int."
                    raise TypeError(error_message)

    @property
    def state(self) -> Set[Coordinate]:
        """
        returns state

        :returns state
        """
        return self.__state

    def next_state(self) -> None:
        """
        updates state by applying the rules of the game

        :returns None
        """
        def region(coordinate: Coordinate) -> List[Coordinate]:
            """
            returns the list of coordinates of the region around the given coordinate

            The region around a given coordinate is defined here to be the union of a) the Moore
            neighbourhood around the given coordinate and b) the given coordinate itself. In other
            words, the region around a coordinate is the coordinate itself plus the 8 closest other
            coordinates.

            :param coordinate: a tuple of form (x, y) giving the coordinate of a live cell in state

            :returns the list of coordinates of the region around the given coordinate
            """
            offsets = range(-1, 2)
            region = [
                Coordinate(coordinate.x + row_offset, coordinate.y + col_offset)
                for row_offset in offsets for col_offset in offsets
            ]
            return region

        candidates = functools.reduce(operator.iconcat, map(region, self.__state), [])
        counted_candidates = collections.Counter(candidates)
        next_state = {
            coordinate for coordinate, count in counted_candidates.items()
            if count == 3 or (count == 4 and coordinate in self.__state)
        }
        self.__state = next_state
