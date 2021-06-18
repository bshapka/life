from typing import List

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
        pass