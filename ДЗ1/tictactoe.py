""" Данный файл содержит запуск игры """

class TicTacGame:
    """ Игра крестики-нолики """

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = 'x'

    def show_board(self):
        """ Отрисовывает текущее состояние доски """
        for i in range(3):
            print('-'*13)
            print('|', self.board[0+3*i], '|', self.board[1+3*i], '|', self.board[2+3*i], '|')
        print('-'*13)

    def empty_cells(self):
        """ Проверяет, остались ли свободные клетки на доске.
        Возвращает True, если остались, иначе - False """
        for i in range(9):
            if self.board[i] == i+1:
                return True
        return False

    def validate_input(self, move):
        """ Проверка ввода пользователя.
        Возвращает True,
        если было введено целое число от 1 до 9
        и данная клетка поля не занята """
        try:
            move = int(move)
        except ValueError:
            print("Вы ввели не целое число. Попробуйте ещё раз.")
            return False
        if move in range(1, 10):
            if self.board[move - 1] == move:
                return True
            print("Данная клетка уже занята, выберите другую.")
            return False
        print("Недопустимое число. Попробуйте ещё раз.")
        return False

    def check_winner(self):
        """ Проверка на победу х или 0.
        Возвращает х или 0 в случае победы, иначе - False """
        for i in range(3):
            if self.board[0+3*i] == self.board[1+3*i] == self.board[2+3*i]:
                return self.board[0+3*i]
            if self.board[i+3*0] == self.board[i+3*1] == self.board[i+3*2]:
                return self.board[i+3*0]
        if (self.board[0] == self.board[4] == self.board[8] or
            self.board[2] == self.board[4] == self.board[6]):
            return self.board[4]
        return False

    def start_game(self):
        """ Регулирует процесс игры """
        while self.empty_cells():
            self.show_board()
            print(self.player + ", сделайте ход.")
            move = input()
            while not self.validate_input(move):
                move = input()
            self.board[int(move)-1] = self.player
            if self.check_winner():
                self.show_board()
                print("Поздравляем " + self.player + " с победой!")
                return
            self.player = '0' if self.player == 'x' else 'x'
        self.show_board()
        print("Ничья!")

if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
