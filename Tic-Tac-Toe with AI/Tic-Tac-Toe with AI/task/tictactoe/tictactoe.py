import random

CORDS = {'1 3': 0, '2 3': 1, '3 3': 2,
         '1 2': 3, '2 2': 4, '3 2': 5,
         '1 1': 6, '2 1': 7, '3 1': 8
         }


class GameFrame:
    def __init__(self):
        self.frame = list("         ")

    def reset_frame(self, new_frame="         "):
        self.frame = list(new_frame)

    def get_frame(self):
        return self.frame

    def set_frame(self, position, symbol):
        self.frame[position] = symbol

    def draw_frame(self):
        print("---------")
        print(f"| {self.frame[0]} {self.frame[1]} {self.frame[2]} |")
        print(f"| {self.frame[3]} {self.frame[4]} {self.frame[5]} |")
        print(f"| {self.frame[6]} {self.frame[7]} {self.frame[8]} |")
        print("---------")


class GameState:
    def __init__(self):
        self.state = "Game not finished"

    def reset_state(self, new_state="Game not finished"):
        self.state = new_state

    def get_state(self):
        return self.state

    def check_state_of_frame(self, frame):
        if self.has_three_o(frame):
            self.state = "O wins"
        elif self.has_three_x(frame):
            self.state = "X wins"
        elif self.has_empty_cell(frame):
            self.state = "Game not finished"
        else:
            self.state = "Draw"

    def has_three_x(self, frame):
        return any(map(lambda x: True if 'XXX' in x else False, self.all_rows(frame)))

    def has_three_o(self, frame):
        return any(map(lambda x: True if 'OOO' in x else False, self.all_rows(frame)))

    def has_empty_cell(self, frame):
        return any(map(lambda x: True if ' ' in x else False, self.all_rows(frame)))

    @staticmethod
    def all_rows(frame):
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [6, 4, 2]]

        return [''.join([frame[element] for element in row]) for row in rows]


class Player:
    def next_move(self, frame):
        pass

    @staticmethod
    def next_symbol(frame):
        num_of_o = sum(map(lambda x: 1 if 'O' in x else 0, frame))
        num_of_x = sum(map(lambda x: 1 if 'X' in x else 0, frame))
        return 'X' if num_of_x <= num_of_o else 'O'


class User(Player):
    def next_move(self, frame):
        symbol = self.next_symbol(frame)
        while True:
            string = input("Enter the coordinates: ")
            if self.is_valid_input(string, frame):
                break
        return CORDS[string], symbol

    @staticmethod
    def is_valid_input(string, frame):

        if not all(x.isnumeric() for x in string.split()):
            print("You should enter numbers!")
            return False
        if len(string) != 3:
            print("Please enter two numbers!")
            return False
        if not all((0 < int(x) < 4) for x in string.split()):
            print("Coordinates should be from 1 to 3!")
            return False
        if frame[CORDS[string]] != ' ':
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True


class Easy(Player):
    def next_move(self, frame):
        print(f'Making move level "easy"')
        return self.random_coordinates(frame), self.next_symbol(frame)

    @staticmethod
    def random_coordinates(frame):
        while True:
            coordinates = random.randint(0, 8)
            if frame[coordinates] == ' ':
                break
        return coordinates


class Medium(Easy):
    def next_move(self, frame):
        my_symbol = self.next_symbol(frame)
        opponent_symbol = 'X' if my_symbol == 'O' else 'O'
        print(f'Making move level "medium"')

        my_winning_move_coordinate = self.can_win_next_move(my_symbol, frame)
        opponent_winning_move_coordinate = self.can_win_next_move(opponent_symbol, frame)

        if my_winning_move_coordinate is not None:
            return my_winning_move_coordinate, my_symbol
        elif opponent_winning_move_coordinate is not None:
            return opponent_winning_move_coordinate, my_symbol
        else:
            return self.random_coordinates(frame), my_symbol

    @staticmethod
    def can_win_next_move(symbol, frame):

        possible_next_move = [[symbol if i == j else frame[i] for i in range(9)]
                              for j in range(9)]

        if symbol == 'X':
            for i in range(9):
                if frame[i] == ' ' and GameState().has_three_x(possible_next_move[i]):
                    return i

        if symbol == 'O':
            for i in range(9):
                if frame[i] == ' ' and GameState().has_three_o(possible_next_move[i]):
                    return i

        return None


class Hard(Player):
    def next_move(self, frame):
        my_symbol = self.next_symbol(frame)
        print(f'Making move level "hard"')

        best_score = float('-inf')
        best_move = None

        for i in range(len(frame)):
            if frame[i] == ' ':
                frame[i] = my_symbol
                score = min_max(frame, depth=0, is_maximizing=False, my_symbol=my_symbol)
                frame[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        print(best_move)
        return best_move, my_symbol


def min_max(frame, depth, is_maximizing, my_symbol):

    opponent_symbol = 'X' if my_symbol == 'O' else 'O'
    state = GameState()
    score = None
    if my_symbol == 'X':
        if state.has_three_x(frame):
            score = 1
        elif state.has_three_o(frame):
            score = -1
        elif not state.has_empty_cell(frame):
            score = 0
    else:
        if state.has_three_x(frame):
            score = -1
        elif state.has_three_o(frame):
            score = 1
        elif not state.has_empty_cell(frame):
            score = 0

    if score is not None:
        return score

    if is_maximizing:
        best_score = float('-inf')
        for i in range(len(frame)):
            if frame[i] == ' ':
                frame[i] = my_symbol
                score = min_max(frame, depth=depth+1, is_maximizing=False, my_symbol=my_symbol)
                frame[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('+inf')
        for i in range(len(frame)):
            if frame[i] == ' ':
                frame[i] = opponent_symbol
                score = min_max(frame, depth=depth+1, is_maximizing=True, my_symbol=my_symbol)
                frame[i] = ' '
                best_score = min(score, best_score)
        return best_score


class TicTacToe:
    def __init__(self):
        self.state = GameState()
        self.frame = GameFrame()
        self.player1 = None
        self.player2 = None

    def start(self):
        self.frame.draw_frame()

        while True:
            self.frame.set_frame(*self.player1.next_move(self.frame.get_frame()))
            self.frame.draw_frame()
            self.state.check_state_of_frame(self.frame.get_frame())
            if self.state.get_state() != "Game not finished":
                break
            self.frame.set_frame(*self.player2.next_move(self.frame.get_frame()))
            self.frame.draw_frame()
            self.state.check_state_of_frame(self.frame.get_frame())
            if self.state.get_state() != "Game not finished":
                break

        print(self.state.get_state())
        self.frame.reset_frame()
        self.state.reset_state()

    def menu(self):
        game_mode = {'user': User(),
                     'easy': Easy(),
                     'medium': Medium(),
                     'hard': Hard()}

        while True:
            _input = input()
            if _input == 'exit':
                break
            _input = _input.split()
            if len(_input) == 3 and _input[0] == 'start' and all(x in game_mode for x in _input[1:]):
                self.player1 = game_mode[_input[1]]
                self.player2 = game_mode[_input[2]]
                self.start()
            else:
                print("Bad parameters")


game = TicTacToe()
game.menu()
