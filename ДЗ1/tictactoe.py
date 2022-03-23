""" Данный файл содержит запуск игры """

class TicTacGame:
    """ Игра крестики-нолики """

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = '0'

    def show_board(self):
        """ Отрисовывает текущее состояние доски """
        for i in range(3):
            print('-'*13)
            print('|', self.board[0+3*i], '|', self.board[1+3*i], '|', self.board[2+3*i], '|')
        print('-'*13)

    @staticmethod
    def validate_input(move):
        """ Проверка ввода пользователя.
        Возвращает True,
        если было введено целое число от 1 до 9 """
        try:
            move = int(move)
        except ValueError:
            print("Вы ввели не целое число. Попробуйте ещё раз.")
            return False
        if move in range(1, 10):
            return True
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
        while not self.check_winner():
            if self.player == 'x':
                self.player = '0'
            else:
                self.player = 'x'
            self.show_board()
            print(self.player + ", сделайте ход.")
            move = input()
            while not self.validate_input(move):
                move = input()
            move = int(move)
            self.board[move-1] = self.player
        self.show_board()
        print("Поздравляем " + self.player + " с победой!")

if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
