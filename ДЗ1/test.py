""" Тесты для игры в крестики-нолики """
import unittest
from tictactoe import TicTacGame

class TestTicTacGame(unittest.TestCase):
    """ Класс, содержащий тесты для функций
    validate_input и check_winner"""
    def test_validate_input_correct(self):
        """ Тест validate_input корректным числом """
        game = TicTacGame()
        self.assertTrue(game.validate_input(9))

    def test_validate_input_uncorrect(self):
        """ Тест validate_input целым числом,
        не попадающим в диапазон от 1 до 9 """
        game = TicTacGame()
        self.assertFalse(game.validate_input(0))

    def test_validate_input_word(self):
        """ Тест validate_input """
        game = TicTacGame()
        self.assertFalse(game.validate_input('ppp'))

    def test_validate_input_float(self):
        """ Тест validate_input дробным числом"""
        game = TicTacGame()
        self.assertFalse(game.validate_input('5.5'))

    def test_check_winner_false(self):
        """ Тест check_winner, карта без победителя """
        game = TicTacGame()
        game.board = [1, 'x', 3, 4, 5, 6, 7, 8, '0']
        self.assertFalse(game.check_winner())

    def test_check_winner_row(self):
        """ Тест check_winner, победитель в строке """
        game = TicTacGame()
        game.board = [1, '0', 3, 'x', 'x', 'x', 7, 8, '0']
        self.assertEqual(game.check_winner(), 'x')

    def test_check_winner_column(self):
        """ Тест check_winner, победитель в столбце """
        game = TicTacGame()
        game.board = [1, '0', 3, 'x', '0', 'x', 7, '0', 9]
        self.assertEqual(game.check_winner(), '0')

    def test_check_winner_diagonal(self):
        """ Тест check_winner, победитель по диагонали """
        game = TicTacGame()
        game.board = ['0', '0', 'x', 4, 'x', 6, 'x', 8, 9]
        self.assertEqual(game.check_winner(), 'x')

if __name__ == '__main__':
    unittest.main()
