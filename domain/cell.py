class Cell:
    """

    Cell class
    >Has 2 attributes:
        - _is_occupied: to signal whether that cell has been turned into a human/AI-type cell
        - _cell_type: has one of the values 0 (for an AI-type cell), 1(for a human-type cell) and None(for a
        non-occupied cell)
    >Each element on the board will be a Cell-type object

    """
    def __init__(self):
        self._is_occupied = False
        self._cell_type = None

    @property
    def cell_type(self):
        return self._cell_type

    @cell_type.setter
    def cell_type(self, value):
        # value must be either 1 (for player type cell) or 0 (for AI type cell)
        self._cell_type = value

    @property
    def occupied(self):
        return self._is_occupied

    @occupied.setter
    def occupied(self, value):
        self._is_occupied = value

    def __str__(self):
        if self._cell_type == 1:  # player type cell
            return "●"
        elif self._cell_type == 0:  # AI type cell
            return "⨁"
        else:
            return "○"
