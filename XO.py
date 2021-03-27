import keyboard
import os


class Game():
    def __init__(self):
        self.turn = 1
        self.mass = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.main_menu()

    def main_menu(self):
        print('')
        print('  Добро пожаловать в игру Крестики-Нолики')
        print('  Вы хотите сыграть против игрока(Enter) или компьютера(+)?')
        print('  Чтобы выбрать нажмите нужную клавишу на клавиатуре')
        keyboard.hook(self.menu_pressed_keys)

    def menu_pressed_keys(button):
        if button.name == 'enter' and button.event_type == 'down':
            os.system("cls")
            self.player_game()
        elif button.name == '+' and button.event_type == 'down':
            os.system("cls")
            print('')
            print('  Coming soon...')

    def player_game(self):
        keyboard.hook(game_pressed_keys)
        game_print(self.mass)

    def turn_game(self):
        if self.turn == 1:
            self.turn = 2
            return 'X'
        else:
            self.turn = 1
            return 'O'

    def game_pressed_keys(button):
        if button.name == '1' and button.event_type == 'down' and self.mass[2][0] == ' ':
            self.mass[2][0] = turn_game()
            game_print(self.mass)
        elif button.name == '2' and button.event_type == 'down' and self.mass[2][1] == ' ':
            self.mass[2][1] = turn_game()
            game_print(mass)
        elif button.name == '3' and button.event_type == 'down' and self.mass[2][2] == ' ':
            self.mass[2][2] = turn_game()
            game_print(mass)
        elif button.name == '4' and button.event_type == 'down' and self.mass[1][0] == ' ':
            self.mass[1][0] = turn_game()
            game_print(mass)
        elif button.name == '5' and button.event_type == 'down' and self.mass[1][1] == ' ':
            self.mass[1][1] = turn_game()
            game_print(mass)
        elif button.name == '6' and button.event_type == 'down' and self.mass[1][2] == ' ':
            self.mass[1][2] = turn_game()
            game_print(mass)
        elif button.name == '7' and button.event_type == 'down' and self.mass[0][0] == ' ':
            self.mass[0][0] = turn_game()
            game_print(mass)
        elif button.name == '8' and button.event_type == 'down' and self.mass[0][1] == ' ':
            self.mass[0][1] = turn_game()
            game_print(mass)
        elif button.name == '9' and button.event_type == 'down' and self.mass[0][2] == ' ':
            self.mass[0][2] = turn_game()
            game_print(mass)
        else:
            pass

    def game_print():
        os.system("cls")
        if not end_game():
            print('')
            print('               Ход Игрока -  {}            '.format(self.turn))
            print('                 Игрок 1 - X ')
            print('                 Игрок 2 - O ')
            print('               -------------')
            for ii in range(3):
                print(
                    '''               | {} | {} | {} |
               -------------'''.format(self.mass[ii][0], self.mass[ii][1], self.mass[ii][2]), sep='   ')
            print('')
            print('  Чтобы выбрать ячейку для вставки символа X или 0,')
            print('  нужно нажать на цифру на NUM LOCK - номер ячейки')
            print('  Esc - для выхода')
        else:
            keyboard.hook(menu_pressed_keys)
            if self.turn == 1:
                self.turn = 2
                char_win = '0'
            else:
                self.turn = 1
                char_win = 'X'
            print('')
            print('               Победил Игрок -  {}            '.format(self.turn))
            print('                 Игрок 1 - X ')
            print('                 Игрок 2 - O ')
            print('               -------------')
            for ii in range(3):
                print(
                    '''               | {} | {} | {} |
               -------------'''.format(char_win, char_win, char_win))
            print(' ')
            print('  Enter - повторить')
            print('  + - сыграть с компьютером')
            print('  Esc - для выхода')
            self.turn = 1
            self.mass = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def end_game(self):
        if self.mass[0][0] == 'X' and self.mass[1][0] == 'X' and self.mass[2][0] == 'X':
            return True
        elif self.mass[0][1] == 'X' and self.mass[1][1] == 'X' and self.mass[2][1] == 'X':
            return True
        elif self.mass[0][2] == 'X' and self.mass[1][2] == 'X' and self.mass[2][2] == 'X':
            return True

        elif self.mass[0][0] == 'X' and self.mass[0][1] == 'X' and self.mass[0][2] == 'X':
            return True
        elif self.mass[1][0] == 'X' and self.mass[1][1] == 'X' and self.mass[1][2] == 'X':
            return True
        elif self.mass[2][0] == 'X' and self.mass[2][1] == 'X' and self.mass[2][2] == 'X':
            return True

        elif self.mass[0][0] == 'X' and self.mass[1][1] == 'X' and self.mass[2][2] == 'X':
            return True
        elif self.mass[0][2] == 'X' and self.mass[1][1] == 'X' and self.mass[2][0] == 'X':
            return True

        elif self.mass[0][0] == 'O' and self.mass[1][0] == 'O' and self.mass[2][0] == 'O':
            return True
        elif self.mass[0][1] == 'O' and self.mass[1][1] == 'O' and self.mass[2][1] == 'O':
            return True
        elif self.mass[0][2] == 'O' and self.mass[1][2] == 'O' and self.mass[2][2] == 'O':
            return True

        elif self.mass[0][0] == 'O' and self.mass[0][1] == 'O' and self.mass[0][2] == 'O':
            return True
        elif self.mass[1][0] == 'O' and self.mass[1][1] == 'O' and self.mass[1][2] == 'O':
            return True
        elif self.mass[2][0] == 'O' and self.mass[2][1] == 'O' and self.mass[2][2] == 'O':
            return True

        elif self.mass[0][0] == 'O' and self.mass[1][1] == 'O' and self.mass[2][2] == 'O':
            return True
        elif self.mass[0][2] == 'O' and self.mass[1][1] == 'O' and self.mass[2][0] == 'O':
            return True
        else:
            return False

    keyboard.wait('esc')


Game()
