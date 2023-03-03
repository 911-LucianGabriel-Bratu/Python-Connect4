from domain.board import Board
import random


class BoardException(Exception):
    pass


class WinException(Exception):
    pass


class Repository:
    def __init__(self):
        self._board = Board()

    def player_step(self, x):
        """
        Function called everytime there is a new input. Checks the availability on a column and adds a player-type cell
        on the most lowest position on that column. It also calls the player_won function to check whether that input
        caused the program to stop.
        :param x: column on which the player element will be inserted
        :return: modifies the type of a cell in the board whether the input was good or not and may cause the program to
        end if that input fulfils the win condition
        """
        if x > 6 or x < 0:
            raise BoardException("Invalid x input")
        y = 5
        while self._board.map[y][x].occupied and not y == -1:
            y -= 1
        if y == -1:
            raise BoardException("No more room on column " + str(x))
        self._board.map[y][x].cell_type = 1
        self._board.map[y][x].occupied = True
        if self.player_won(x, y):
            raise WinException("Player won!")

    def player_won(self, x, y):
        """
        Function called when checking whether an element that was added to the board fulfils the win condition
        :param x: column on which to check
        :param y: line on which to check
        :return: True, if the element has 3 other player-type cells in its neighbourhood. False otherwise.
        """
        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        # check all the elements on the left of the current position
        while x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy -= 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        # check all the elements on the right of the current position
        while x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy += 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        y_copy -= 1
        # check all the elements below the current position
        while y_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            y_copy -= 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        y_copy += 1
        # check all the elements above the current position
        while y_copy <= 5 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            y_copy += 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy += 1
        # check all the elements in a diagonal to the right above the current position
        while y_copy <= 5 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy += 1
            y_copy += 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy += 1
        # check all the elements in a diagonal to the left above the current position
        while y_copy <= 5 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy -= 1
            y_copy += 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy -= 1
        # check all the elements in a diagonal to the right below the current position
        while y_copy >= 0 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy += 1
            y_copy -= 1
        if player_elements == 4:
            return True

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy -= 1
        # check all the elements in a diagonal to the left below the current position
        while y_copy >= 0 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 4:
            player_elements += 1
            x_copy -= 1
            y_copy -= 1
        if player_elements == 4:
            return True

        return False

    """
    
    AI function section
        > AI will check if there are any 3 player-type cells next to each other and will attempt to block the 4th one
        that the human player could insert
        
        > AI will check for its own win condition and will add an element to fulfil the win condition. Otherwise, it 
        will add an element next to an existing one if possible.
        
        > If none of the above cases are met (it's the first time the AI moves), the AI will insert at a random position
    
    """

    def ai_player_elements_checker(self, x, y):
        """
        The first function called each time the AI needs to make a move. Checks whether there is a case in which the
        human player has 3 elements next to each other and the AI can prevent the human player from winning.
        :param x: x coordinate on the board
        :param y: y coordinate on the board
        :return: the column on which the AI can insert the element (integer)
        """
        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        # check all the elements on the left of the current position
        while x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy -= 1
        if player_elements == 3:
            if x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type is None:
                if y_copy + 1 <= 5:
                    if not self._board.map[y_copy + 1][x_copy].cell_type is None:
                        return x_copy
                elif y_copy == 5:
                    return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        # check all the elements on the right of the current position
        while x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy += 1
        if player_elements == 3:
            if x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type is None:
                if y_copy + 1 <= 5:
                    if not self._board.map[y_copy + 1][x_copy].cell_type is None:
                        return x_copy
                elif y_copy == 5:
                    return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        y_copy += 1
        # check all the elements below the current position
        while y_copy <= 5 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            y_copy += 1
        if player_elements == 3:
            if y - 1 >= 0:
                if self._board.map[y - 1][x_copy].cell_type is None:
                    return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        y_copy -= 1
        # check all the elements above the current position
        while y_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            y_copy -= 1
        if player_elements == 3:
            if y_copy >= 0 and self._board.map[y_copy][x_copy].cell_type is None:
                return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy -= 1
        # check all the elements in a diagonal to the right above the current position
        while y_copy >= 0 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy += 1
            y_copy -= 1
        if player_elements == 3:
            if x_copy <= 6 and y_copy >= 0:
                if self._board[y_copy][x_copy].cell_type is None:
                    if y_copy + 1 <= 5:
                        if not self._board[y_copy + 1][x_copy].cell_type is None:
                            return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy -= 1
        # check all the elements in a diagonal to the left above the current position
        while y_copy >= 0 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy -= 1
            y_copy -= 1
        if player_elements == 3:
            if x_copy >= 0 and y_copy >= 0:
                if self._board[y_copy][x_copy].cell_type is None:
                    if y_copy + 1 <= 5:
                        if not self._board[y_copy + 1][x_copy].cell_type is None:
                            return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy += 1
        # check all the elements in a diagonal to the left below the current position
        while y_copy <= 5 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy -= 1
            y_copy += 1
        if player_elements == 3:
            if x_copy >= 0 and y_copy <= 5:
                if self._board[y_copy][x_copy].cell_type is None:
                    if y_copy + 1 <= 5:
                        if not self._board[y_copy + 1][x_copy].cell_type is None:
                            return x_copy

        player_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy += 1
        # check all the elements in a diagonal to the right below the current position
        while y_copy <= 5 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 1 and player_elements < 3:
            player_elements += 1
            x_copy += 1
            y_copy += 1
        if player_elements == 3:
            if x_copy <= 6 and y_copy <= 5:
                if self._board[y_copy][x_copy].cell_type is None:
                    if y_copy + 1 <= 5:
                        if not self._board[y_copy + 1][x_copy].cell_type is None:
                            return x_copy
        return False

    def ai_player_block_checker(self):
        """
        Function that goes through and calls "ai_player_elements_checker" for every cell on the board
        :return: the first column on which the AI can insert an element to prevent the human from winning (integer)
        """
        for x in range(7):
            for y in range(6):
                if self._board[y][x].cell_type == 1:
                    ai_x = self.ai_player_elements_checker(x, y)
                    if ai_x:
                        return ai_x
        return False

    def ai_player_block(self):
        """
        Function used when the column on which the AI can insert the element has been found. Used for setting the
        "cell_type" and "occupied" attributes.
        :return: x and y coordinates of the AI-type element inserted (integers)
        """
        ai_x = self.ai_player_block_checker()
        if ai_x:
            ai_y = 5
            while self._board.map[ai_y][ai_x].occupied and not ai_y == -1:
                ai_y -= 1
            if ai_y == -1:
                return False
            else:
                self._board[ai_y][ai_x].cell_type = 0
                self._board[ai_y][ai_x].occupied = True
                return ai_x, ai_y
        return False

    def ai_step(self):
        """
        Function called when AI needs to make a move. Calls the check functions and when found, the AI element is set.
        If the check functions don't return a position, the next attempt is to find another AI-type cell and add next
        to it.
        If this other case is not met, the AI will add to a random column.
        :return: column on which the AI inserted (integer)
                 can also raise a "WinException" in the case that the move that the AI executed generated a win case.
        """
        try:
            ai_x, ai_y = self.ai_player_block()
            xy_found = True
        except TypeError:
            xy_found = False
        if not xy_found:
            xy_found = False
            for x in range(7):
                for y in range(6):
                    if self._board[y][x].cell_type == 0:
                        if y - 1 >= 0:
                            if self._board[y - 1][x].cell_type is None:
                                ai_x = x
                                ai_y = y - 1
                                xy_found = True
                        elif x - 1 >= 0 and y + 1 <= 5:
                            if self._board[y][x - 1].cell_type is None and not self._board[y + 1][
                                                                                   x - 1].cell_type is None:
                                ai_x = x - 1
                                ai_y = y
                                xy_found = True
                        elif x + 1 <= 6 and y + 1 <= 5:
                            if self._board[y][x + 1].cell_type is None and not self._board[y + 1][
                                                                                   x + 1].cell_type is None:
                                ai_x = x + 1
                                ai_y = y
                                xy_found = True
            if not xy_found:
                while not xy_found:
                    ai_x = random.randint(0, 6)
                    ai_y = 5
                    while not self._board[ai_y][ai_x].cell_type is None and ai_y > -1:
                        ai_y -= 1
                    if not ai_y == -1:
                        xy_found = True

        self._board[ai_y][ai_x].cell_type = 0
        self._board[ai_y][ai_x].occupied = True
        if self.ai_won(ai_x, ai_y):
            raise WinException("AI won!")
        return ai_x

    def ai_won(self, x, y):
        """
        Function used in checking for a win case with respect to the AI elements.
        :param x: column coordinate
        :param y: line coordinate
        :return: True, if there is a case in which 4 elements of AI-type are next to each other. False otherwise.
        """
        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        # check all the elements on the left of the current position
        while x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy -= 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        # check all the elements on the right of the current position
        while x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy += 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        y_copy += 1
        # check all the elements below the current position
        while y_copy <= 5 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            y_copy += 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        y_copy -= 1
        # check all the elements above the current position
        while y_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            y_copy -= 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy -= 1
        # check all the elements in a diagonal to the right above the current position
        while y_copy >= 0 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy += 1
            y_copy -= 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy -= 1
        # check all the elements in a diagonal to the left above the current position
        while y_copy >= 0 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy -= 1
            y_copy -= 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy -= 1
        y_copy += 1
        # check all the elements in a diagonal to the left below the current position
        while y_copy <= 5 and x_copy >= 0 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy -= 1
            y_copy += 1
        if ai_elements == 4:
            return True

        ai_elements = 1
        x_copy = x
        y_copy = y
        x_copy += 1
        y_copy += 1
        # check all the elements in a diagonal to the right below the current position
        while y_copy <= 5 and x_copy <= 6 and self._board.map[y_copy][x_copy].cell_type == 0 and ai_elements < 4:
            ai_elements += 1
            x_copy += 1
            y_copy += 1
        if ai_elements == 4:
            return True

        return False

    def board_filled_checker(self):
        """
        Function used in checking whether the board has been filled or not
        :return: True if it has been filled, False otherwise.
        """
        found = False
        for x in range(7):
            for y in range(6):
                if self._board[y][x].cell_type is None:
                    found = True
        if found == False:
            return True
        return False

    def __str__(self):
        return str(self._board)
