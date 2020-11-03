import random


class RPS:
    def __init__(self):
        self.file = 'rating.txt'
        # self.make_sb_file()

        self.rule_set = ['rock', 'paper', 'scissors']
        self.scoreboard = {}
        self.player_name = ''
        self.player_score = 0

    def start(self):
        self.get_scoreboard()
        self.create_player()
        self.set_rules()

        while True:
            if choice := input():
                if choice == '!exit':
                    print("Bye!")
                    break
                elif choice == '!rating':
                    print(f"Your rating: {self.player_score}")
                else:
                    try:
                        self.evaluate(choice)
                    except AssertionError:
                        print("Invalid input")

        # self.update_scoreboard()
        # self.upload_scoreboard()

    def make_sb_file(self):
        file = open(self.file, 'a')
        file.close()

    def create_player(self):
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}")

        if self.player_name in self.scoreboard:
            self.player_score = int(self.scoreboard[self.player_name])

    def set_rules(self):
        if (chosen_rule_set := input().split(',')) != ['']:
            self.rule_set = chosen_rule_set
        print(self.rule_set)
        print("Okay, let's start")

    def get_scoreboard(self):
        file = open(self.file, 'r')
        for line in file:
            name, score = line.split()
            self.scoreboard[name] = score
        file.close()

    def upload_scoreboard(self):
        file = open(self.file, 'w')
        for player, score in self.scoreboard.items():
            file.write(f"{player} {score}\n")
        file.close()

    def update_scoreboard(self):
        self.scoreboard[self.player_name] = str(self.player_score)

    def a_beats_b(self, a, b):
        a_beats = [self.rule_set[i]
                   for i in range(self.rule_set.index(a) - len(self.rule_set) // 2,
                                  self.rule_set.index(a))]

        return b in a_beats

    def evaluate(self, choice):
        assert choice in self.rule_set
        computer = random.choice(self.rule_set)

        if computer == choice:
            print(f"There is a draw ({choice})")
            self.player_score += 50
        elif self.a_beats_b(computer, choice):
            print(f"Sorry, but the computer chose {computer}")
        else:
            print(f"Well done. The computer chose {computer} and failed")
            self.player_score += 100


game = RPS()
game.start()
