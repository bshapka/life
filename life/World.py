from typing import List, Tuple, Set


class World:
    """
    Represents a 2D world in grid form with each cell in the grid being live or dead (but not both)

    Fields:
        state: Set[Tuple[int, int]]
            represents the state of the world as a set of 2-integer tuples. Each element of the set
            gives the coordinates of a live cell in the grid. As such, the coordinates of dead cells
            are not part of the state.

    Methods:
        next_state() -> None
            updates state by applying the rules of the game

        get_state() -> Set[Tuple[int, int]]
            returns state
    """

    def __init__(self, initial_state: Set[Tuple[int, int]]) -> None:
        """
        Instantiates a World

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

    def get_state(self) -> List[List[bool]]:
        """
        returns state

        :returns state
        """
        return self.state

    def get_dimensions(self) -> Tuple[int, int]:
        """
        Returns the dimensions of the state as a tuple of form (length, width)

        assumes: state is not a jagged array

        :returns the dimensions of the state as a tuple of form (length, width)
        """
        dimensions = (0, 0)
        if self.state:
            dimensions = (len(self.state[0]), len(self.state))
        return dimensions

    def next_state(self) -> None:
        """
        Updates state by applying the rules of the game to all elements of state

        :returns None
        """
        self.state = [
            [self.__next_cell((i, j), is_live) for j, is_live in enumerate(row)]
            for i, row in enumerate(self.state)
        ]

    def __next_cell(self, coordinate: Tuple[int, int], is_live: bool) -> bool:
        """
        Returns next cell at given coordinate by applying the rules of the game

        :param coordinate: a tuple of form (row index, column index) giving the coordinate of a
        cell in state

        :param is_live: the state of the cell (True if live, False if dead)

        :returns next cell at given coordinate by applying the rules of the game
        """
        live_neighbour_count = self.__live_neighbour_count(coordinate)
        stays_live = is_live and live_neighbour_count in {2, 3}
        is_born = not is_live and live_neighbour_count == 3
        return stays_live or is_born

    def __live_neighbour_count(self, coordinate: Tuple[int, int]) -> int:
        """
        Returns count of live neighbouring cells to cell with given coordinate

        :param coordinate: a tuple of form (row index, column index) giving the coordinate of a
        cell in state

        :returns count of live neighbouring cells to cell with given coordinate
        """
        row_index, col_index = coordinate
        offsets = range(-1, 2)
        neighbours = [
            self.__get_cell((row_index + row_offset, col_index + col_offset))
            for row_offset in offsets for col_offset in offsets
            if not row_offset == col_offset == 0
            and self.__is_valid_coordinate((row_index + row_offset, col_index + col_offset))
        ]
        return sum(neighbours)

    def __is_valid_coordinate(self, coordinate: Tuple[int, int]) -> bool:
        """
        Returns True if given coordinate is within state, else returns False

        :param coordinate: a tuple of form (row index, column index) potentially giving the
        coordinate of a cell in the state

        :returns True if given coordinate is within state, else returns False
        """
        min_row_index = min_col_index = 0
        length, width = self.get_dimensions()
        max_row_index, max_col_index = width - 1, length - 1

        row_index, col_index = coordinate
        is_valid_row_index = min_row_index <= row_index <= max_row_index
        is_valid_col_index = min_col_index <= col_index <= max_col_index
        return is_valid_row_index and is_valid_col_index

    def __get_cell(self, coordinate: Tuple[int, int]) -> bool:
        """
        Returns cell in state corresponding to given coordinate

        :param coordinate: a tuple of form (row index, column index) giving the coordinate of a
        cell in the state

        :returns cell in state corresponding to given coordinate
        """
        row_index, col_index = coordinate
        return self.state[row_index][col_index]
