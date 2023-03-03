import unittest
from domain.cell import Cell
from domain.board import Board
from repo.repo import Repository


class CellTest(unittest.TestCase):
    def setUp(self) -> None:
        self._cell = Cell()

    def tearDown(self) -> None:
        pass

    def cell_domain_test(self):
        self.assertEqual(self._cell.occupied, False)
        self.assertEqual(self._cell.cell_type, None)
        self.assertEqual(str(self._cell), "○")
        self._cell.cell_type = 0
        self._cell.occupied = True
        self.assertEqual(self._cell.occupied, True)
        self.assertEqual(self._cell.cell_type, 0)
        self.assertEqual(str(self._cell), "⨁")
        self._cell.cell_type = 1
        self.assertEqual(self._cell.cell_type, 1)
        self.assertEqual(str(self._cell), "●")


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board()

    def tearDown(self) -> None:
        pass

    def board_test(self):
        number_of_elements = 0
        for x in range(self._board.columns):
            for y in range(self._board.rows):
                number_of_elements += 1
        self.assertEqual(number_of_elements, 42)


class RepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repository()

    def tearDown(self) -> None:
        pass

    def test_player(self):
        self._repo.player_step(0)
        self._repo.player_step(0)
        self._repo.player_step(0)
        self._repo.player_step(0)
        self.assertEqual(self._repo.player_won(0, 5), True)
        self.assertEqual(self._repo.board_filled_checker(), False)

    def test_ai(self):
        self._repo.ai_step()
        self._repo.ai_step()
        self._repo.ai_step()
        self._repo.ai_step()
        for i in range(7):
            if self._repo.ai_won(i, 5) == True:
                self.assertEqual(self._repo.ai_won(i, 5), True)
