import random
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time for {func.__name__}: {(end_time - start_time):.4f} seconds')
        return result
    return wrapper


def validate_input(func):
    def wrapper(*args, **kwargs):
        player_name = args[1]
        if not player_name.strip():
            raise ValueError('Player name cannot be empty')
        return func(*args, **kwargs)
    return wrapper


class Dice:

    def draw_dice(self, number):
        dices_set = []
        if number == 1:
            dices_set.extend([
                "---------",
                "│       │",
                "│   ●   │",
                "│       │",
                "---------"
            ])
        elif number == 2:
            dices_set.extend([
                "---------",
                "│ ●     │",
                "│       │",
                "│     ● │",
                "---------"
            ])
        elif number == 3:
            dices_set.extend([
                "---------",
                "│ ●     │",
                "│   ●   │",
                "│     ● │",
                "---------"
            ])
        elif number == 4:
            dices_set.extend([
                "---------",
                "│ ●   ● │",
                "│       │",
                "│ ●   ● │",
                "---------"
            ])
        elif number == 5:
            dices_set.extend([
                "---------",
                "│ ●   ● │",
                "│   ●   │",
                "│ ●   ● │",
                "---------"
            ])
        elif number == 6:
            dices_set.extend([
                "---------",
                "│ ● ● ● │",
                "│ ● ● ● │",
                "│ ● ● ● │",
                "---------"
            ])
        else:
            dices_set.append('Invalid dice number')
        return dices_set

    @measure_time
    def dice_rolling(self):
        dice1_number = random.randint(1, 6)
        dice2_number = random.randint(1, 6)

        dice1 = self.draw_dice(dice1_number)
        dice2 = self.draw_dice(dice2_number)

        for line1, line2 in zip(dice1, dice2):
            print(line1, '    ', line2)

        print(f'Points scored: {dice1_number + dice2_number}')
        return dice1_number + dice2_number

class Player:
    @validate_input
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds_played = 0

    def update_score(self, points):
        self.score += points

    def increment_rounds_played(self):
        self.rounds_played += 1

    def __str__(self):
        return f'Player: {self.name}, Score: {self.score}, Rounds Played: {self.rounds_played}'

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice()

    @measure_time
    def play_round(self):
        for _ in range(5):
            print(f'{self.player1.name} is rolling...')
            time.sleep(2)
            self.player1.update_score(self.dice.dice_rolling())
            self.player1.increment_rounds_played()

            print(f'{self.player2.name} is rolling...')
            time.sleep(2)
            self.player2.update_score(self.dice.dice_rolling())
            self.player2.increment_rounds_played()

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            return self.player1
        elif self.player2.score > self.player1.score:
            return self.player2
        else:
            return None


def main():
    player1_name = input('Enter the name of the first player: ')
    player2_name = input('Enter the name of the second player: ')
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    game = Game(player1, player2)
    game.play_round()
    winner = game.determine_winner()
    if winner:
        print(f'The winner is {winner.name} with a score of {winner.score}')
    else:
        print('It\'s a tie!')


if __name__ == '__main__':
    main()