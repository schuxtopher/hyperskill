class GameState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state"""
        if state.name in self.allowed:
            # print(f"Current: {self} => switched to new state {state.name}")
            self.__class__ = state
        # else:
            # print(f"Current: {self} => switching to {state.name} not possible")

    def __str__(self):
        return self.name


class GameNotFinished(GameState):
    """When no side has a three in a row but the field has empty cells"""
    name = "Game not finished"
    allowed = ['Game not finished', 'Draw', 'X wins', 'O wins', 'Impossible']


class Draw(GameState):
    """When no side has a three in a row and the field has no empty cells"""
    name = "Draw"
    allowed = []


class XWins(GameState):
    """When the field has three X in a row"""
    name = "X wins"
    allowed = []


class OWins(GameState):
    """When the field has three O in a row"""
    name = "O wins"
    allowed = []


class TicTacToe(object):
    """ A class representing the TicTacToe game"""

    def __init__(self):
        self.state = GameNotFinished()
        self.frame = []
        self.symbol = 'X'

    def change(self, state):
        """Change state"""
        self.state.switch(state)

    def fill_frame(self, string):
        """Reads 9 symbols from the input and writes an appropriate field.
        can only contain 'X', 'O' and '_' symbols."""

        allowed_chars = ['X', 'O', '_']

        if len(string) != 9:
            print("not 9 symbols")
            return None
        if any(x not in allowed_chars for x in string):
            print("contains not allowed symbols")
            return None

        self.frame = list(string)

    def draw_frame(self):
        symbols = self.frame
        print("---------")
        print(f"| {symbols[0]} {symbols[1]} {symbols[2]} |")
        print(f"| {symbols[3]} {symbols[4]} {symbols[5]} |")
        print(f"| {symbols[6]} {symbols[7]} {symbols[8]} |")
        print("---------")

    def add_symbol(self, string, symbol):
        coordinates = {'1 3': 0, '2 3': 1, '3 3': 2,
                       '1 2': 3, '2 2': 4, '3 2': 5,
                       '1 1': 6, '2 1': 7, '3 1': 8}

        if not all(x.isnumeric() for x in string.split()):
            print("You should enter numbers!")
            return False
        if len(string) != 3:
            print("Please enter two numbers!")
            return False
        if not all((0 < int(x) < 4) for x in string.split()):
            print("Coordinates should be from 1 to 3!")
            return False
        if self.frame[coordinates[string]] != '_':
            print("This cell is occupied! Choose another one!")
            return False
        else:
            self.frame[coordinates[string]] = symbol
            return True

    def start(self):
        self.fill_frame('_________')
        self.draw_frame()
        while True:
            while True:
                if self.add_symbol(input("Enter the coordinates: "), self.symbol):
                    break
            self.symbol = 'O' if self.symbol == 'X' else 'X'
            self.draw_frame()
            self.check_state()
            if self.state.name != "Game not finished":
                break
        print(self.state)

    def check_state(self):
        if self.has_three_o():
            self.change(OWins)

        elif self.has_three_x():
            self.change(XWins)

        elif self.has_empty_cell():
            self.change(GameNotFinished)

        else:
            self.change(Draw)

    def all_rows(self):
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [6, 4, 2]]

        return [''.join([self.frame[element] for element in row]) for row in rows]

    def has_three_x(self):
        return any(element in ['XXX'] for element in self.all_rows())

    def has_three_o(self):
        return any(element in ['OOO'] for element in self.all_rows())

    def has_empty_cell(self):
        return any(element in ['_'] for element in self.frame)


game = TicTacToe()
game.start()
