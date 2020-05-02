"""
module with classes Player and Enemy
"""
import random
from module2.classes.exceptions import GameOver, EnemyDown, RestartGame
from module2.classes.settings import DEFAULT_LIVES_COUNT, ALLOWED_COMMANDS


class Enemy(object):
    """
    class Enemy
    """
    def __init__(self):
        self.level = 1
        self.lives = 1

    @staticmethod
    def select_attack():
        """
        random choice of attack
        """
        return random.randint(1, 3)

    def decrease_lives(self, player):
        """
        life reduction function, depends on Player-obj, created in game function
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player(object):
    """
    class Player
    """
    def __init__(self, name):
        self.name = name
        self.lives = DEFAULT_LIVES_COUNT
        self.score = 0
        self.allowed_attacks = ['1', '2', '3']
        self.level = 1
        self.allowed_commands = ALLOWED_COMMANDS

    def command(self, command):
        """
        function that defines actions depending on the entered command
        """
        if command == self.allowed_commands[0]:
            raise RestartGame
        if command == self.allowed_commands[1]:
            print('Allowed Commands:\nSTART - to restart Game\n'
                  'HELP - to watch allowed commands\n'
                  'SCORE - find out the score\n'
                  'EXIT - Quit Game')
        elif command == self.allowed_commands[2]:
            print(
                'Your score: %s' % self.score
            )
        elif command == self.allowed_commands[3]:
            raise KeyboardInterrupt

    @staticmethod
    def fight(attack, defense):
        """
        function in which the result of the battle is calculated
        """
        if attack == defense:
            score = 0
        elif (attack == 1 and defense == 3) or\
             (attack == 2 and defense == 1) or\
             (attack == 3 and defense == 2):
            score = 1
        else:
            score = -1
        return score

    def decrease_lives(self):
        """
        life reduction function, depends on Enemy-obj, created in game function
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver("Game Over!\nYour final score: %s" % self.score, self)

    def attack(self, enemy_obj):
        """
        accepts user input to attack and Enemy-obj's to defence 'select_attack' function result,
        counts score and lives
        """
        attack = 0
        while attack not in self.allowed_attacks:
            attack = input('Select Attack to Use: 1 - "ROGUE", 2 - "WARRIOR", '
                           '3 - "WIZARD" :\n').lower()
            self.command(attack)
        attack = int(attack)
        defence = enemy_obj.select_attack()
        score = self.fight(attack, defence)
        if score == 0:
            print(
                "It's a draw!"
            )
        elif score == 1:
            print(
                "You attacked successfully!"
            )
            self.score += score
            enemy_obj.decrease_lives(self)
        elif score == -1:
            print(
                "You missed!"
            )

    def defence(self, enemy_obj):
        """
        the same as 'attack' function, but here Enemy-obj attacks and Player-obj defenses
        """
        attack = enemy_obj.select_attack()
        defence = 0
        while defence not in self.allowed_attacks:
            defence = input('Select Defence to Use: 1 - "ROGUE",'
                            ' 2 - "WARRIOR", 3 - "WIZARD"\n').lower()
            self.command(defence)
        defence = int(defence)
        score = self.fight(attack, defence)
        if score == 0:
            print(
                "It's a draw!"
            )
        elif score == 1:
            print(
                "He hit you"
            )
            self.decrease_lives()
        elif score == -1:
            print(
                "You dodged attack!"
            )
