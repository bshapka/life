from typing import List, Tuple


class World:

    def __init__(self, initial_state: List[List[bool]]):
        """
        Instantiates a World

        :raises TypeError if starting_state contains a non-bool

        :raises ValueError if starting_state is a jagged array

        :param starting_state: represents an initial state of the World

        :returns a new World
        """
        self.__validate_state(initial_state)
        self.state = initial_state

    def __validate_state(self, state: List[List[bool]]):
        """
        Validates a given state

        :raises TypeError if starting_state contains a non-bool

        :raises ValueError if starting_state is a jagged array

        :param state: represents a state of the World

        :returns void
        """
        row_lengths = set()
        for row in state:
            row_length = 0
            for cell in row:
                row_length += 1
                if type(cell) is not bool:
                    raise TypeError(
                        "Argument state must be of type List[List[bool]].")
            if row_lengths != set() and row_length not in row_lengths:
                raise ValueError("Argument must not be a jagged array")
            else:
                row_lengths.add(row_length)

    def get_state(self) -> List[List[bool]]:
        """
        returns state

        :param none

        :returns state
        """
        return self.state

    def next_state(self):
        """
        Advances state one generation

        :param none

        :returns void
        """
        self.state = [
            [self.__next_cell((i, j), is_live) for j, is_live in enumerate(row)]
            for i, row in enumerate(self.state)
        ]

    def __next_cell(self, coordinate: Tuple[int, int], is_live: bool) -> bool:
        return False