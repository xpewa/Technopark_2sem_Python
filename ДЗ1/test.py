""" Тесты для игры в крестики-нолики """
import unittest
from tictactoe import TicTacGame

class TestTicTacGame(unittest.TestCase):
    """ Класс, содержащий тесты для функций
    validate_input и check_winner"""
    def test_validate_input_correct2(self):
        """ Тест validate_input корректным числом"""
        game = TicTacGame()
        self.assertTrue(game.validate_input('1'))
        self.assertTrue(game.validate_input('2'))
        self.assertTrue(game.validate_input('3'))
        self.assertTrue(game.validate_input('4'))
        self.assertTrue(game.validate_input('5'))
        self.assertTrue(game.validate_input('6'))
        self.assertTrue(game.validate_input('7'))
        self.assertTrue(game.validate_input('8'))
        self.assertTrue(game.validate_input('9'))

    def test_validate_input_uncorrect_less(self):
        """ Тест validate_input целым числом,
        не попадающим в диапазон от 1 до 9 (меньше) """
        game = TicTacGame()
        self.assertFalse(game.validate_input('0'))

    def test_validate_input_uncorrect_larger(self):
        """ Тест validate_input целым числом,
        не попадающим в диапазон от 1 до 9 (больше) """
        game = TicTacGame()
        self.assertFalse(game.validate_input('100'))

    def test_validate_input_word(self):
        """ Тест validate_input """
        game = TicTacGame()
        self.assertFalse(game.validate_input('ppp'))

    def test_validate_input_float(self):
        """ Тест validate_input дробным числом """
        game = TicTacGame()
        self.assertFalse(game.validate_input('5.5'))

    def test_validate_input_not_free(self):
        """ Тест validate_input занятое поле """
        game = TicTacGame()
        game.board = [1, 'x', 3,
                      4,  5,  6,
                      7,  8,  9]
        self.assertFalse(game.validate_input('2'))

    def test_empty_cells_true(self):
        """ Тест empty_cells при наличии свободных клеток """
        game = TicTacGame()
        self.assertTrue(game.empty_cells())

    def test_empty_cells_false(self):
        """ Тест empty_cells при отсутствии свободных клеток """
        game = TicTacGame()
        game.board = ['x', 'x', '0',
                      '0', '0', 'x',
                      'x', '0', 'x']
        self.assertFalse(game.empty_cells())

    def test_check_winner_false(self):
        """ Тест check_winner, карта без победителя """
        game = TicTacGame()
        game.board = [1, 'x', 3,
                      4,  5,  6,
                      7,  8, '0']
        self.assertFalse(game.check_winner())

    def test_check_winner_row1(self):
        """ Тест check_winner, победитель в строке 1 """
        game = TicTacGame()
        game.board = ['0', '0', '0',
                      'x',  5,  'x',
                      'x',  8,   9]
        self.assertEqual(game.check_winner(), '0')

    def test_check_winner_row2(self):
        """ Тест check_winner, победитель в строке 2 """
        game = TicTacGame()
        game.board = [1,  '0',  3,
                     'x', 'x', 'x',
                      7,   8,  '0']
        self.assertEqual(game.check_winner(), 'x')

    def test_check_winner_row3(self):
        """ Тест check_winner, победитель в строке 3 """
        game = TicTacGame()
        game.board = [1,  '0',  3,
                      4,   5,  '0',
                     'x', 'x', 'x']
        self.assertEqual(game.check_winner(), 'x')

    def test_check_winner_column1(self):
        """ Тест check_winner, победитель в столбце 1 """
        game = TicTacGame()
        game.board = ['x',  2,  3,
                      'x', '0', 6,
                      'x', '0', 9]
        self.assertEqual(game.check_winner(), 'x')

    def test_check_winner_column2(self):
        """ Тест check_winner, победитель в столбце 2 """
        game = TicTacGame()
        game.board = [1,  '0',  3,
                     'x', '0', 'x',
                      7,  '0',  9]
        self.assertEqual(game.check_winner(), '0')

    def test_check_winner_column3(self):
        """ Тест check_winner, победитель в столбце 3 """
        game = TicTacGame()
        game.board = ['x',  2,  '0',
                       4,  'x', '0',
                      'x',  8,  '0']
        self.assertEqual(game.check_winner(), '0')

    def test_check_winner_secondary_diagonal(self):
        """ Тест check_winner, победитель в побочной диагонали """
        game = TicTacGame()
        game.board = ['0', '0', 'x',
                       4,  'x',  6,
                      'x',  8,   9]
        self.assertEqual(game.check_winner(), 'x')

    def test_check_winner_main_diagonal(self):
        """ Тест check_winner, победитель в главной диагонали """
        game = TicTacGame()
        game.board = ['0', 'x', '0',
                      'x', '0', 'x',
                      'x', 'x', '0']
        self.assertEqual(game.check_winner(), '0')

    def test_start_game_draw(self):
        """ Тест start_game на ничью """
        game = TicTacGame()
        game.board = ['x', 'x', '0',
                      '0', '0', 'x',
                      'x', '0', 'x']
        self.assertFalse(game.empty_cells())
        game.start_game()

if __name__ == '__main__':
    unittest.main()
