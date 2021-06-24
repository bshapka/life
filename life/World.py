import collections
import functools
import operator
from typing import List, Tuple, Set


class World:
    """
    represents a 2D world in grid form with each cell in the grid being live or dead (but not both)

    fields:
        state: Set[Tuple[int, int]]
            represents the state of the world as a set of 2-integer tuples. Each element of the set
            gives the coordinates of a live cell in the grid. As such, the coordinates of dead cells
            are not part of the state.

    methods:
        next_state() -> None
            updates state by applying the rules of the game

        get_state() -> Set[Tuple[int, int]]
            returns state
    """

    def __init__(self, initial_state: Set[Tuple[int, int]]) -> None:
        """
        instantiates a World

        :param initial_state: an initial state of the World

        :returns None
        """
        World.__validate_state(initial_state)
        self.state = initial_state

    @staticmethod
    def __validate_state(state: Set[Tuple[int, int]]) -> None:
        """
        validates a given state

        checks that state is of type Set[Tuple[int, int]]

        :raises TypeError if state is not of type Set

        :raises TypeError if any element of state is not of type Tuple

        :raises TypeError if any element of any element of state is not not of type int

        :raises ValueError if any element of state is not not of size 2

        :param state: a state for the World

        :returns None
        """
        error_message = "The state must be of type Set[Tuple[int, int]]. "

        if type(state) is not set:
            error_message += "The collection used is not of type set."
            raise TypeError(error_message)

        for coordinate in state:
            if type(coordinate) is not tuple:
                error_message += "An element of the set is not a tuple."
                raise TypeError(error_message)
            size = 0
            for component in coordinate:
                if type(component) is not int:
                    error_message += "A tuple in the set contains an element that is not of type int."
                    raise TypeError(error_message)
                size += 1
            if size != 2:
                error_message += "A tuple in the set is not of size 2."
                raise ValueError(error_message)

    def get_state(self) -> Set[Tuple[int, int]]:
        """
        returns state

        :returns state
        """
        return self.state

    def next_state(self) -> None:
        """
        updates state by applying the rules of the game

        :returns None
        """
        def region(coordinate: Tuple[int, int]) -> List[Tuple[int, int]]:
            """
            returns the list of coordinates of the region around the given coordinate

            The region around a given coordinate is defined here to be the union of a) the Moore
            neighbourhood around the given coordinate and b) the given coordinate itself. In other
            words, the region around a coordinate is the coordinate itself plus the 8 closest other
            coordinates.

            :param coordinate: a tuple of form (row index, column index) giving the coordinate of a
            live cell in state

            :returns the list of coordinates of the region around the given coordinate
            """
            row_index, col_index = coordinate
            offsets = range(-1, 2)
            region = [
                (row_index + row_offset, col_index + col_offset)
                for row_offset in offsets for col_offset in offsets
            ]
            return region

        candidates = functools.reduce(operator.iconcat, map(region, self.state), [])
        counted_candidates = collections.Counter(candidates)
        next_state = {
            coordinate for coordinate, count in counted_candidates.items()
            if count == 3 or (count == 4 and coordinate in self.state)
        }
        self.state = next_state
