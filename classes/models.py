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
        try:
            self.lives -= 1
            if self.lives == 0:
                raise EnemyDown
        except EnemyDown:
            self.level += 1
            player.score += 5
            player.level += 1
            print('-'
                  * 65)
            print('You killed enemy! Your Score: %s. Level: %s' % (player.score,
                                                                   player.level))
            print('-'
                  * 65)
        else:
            print('Your lives: %s | Enemy lives: %s\n'
                  % (player.lives, self.lives))


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
    def fight(m_1, m_2):
        """
        function in which the result of the battle is calculated
        """
        score = 0
        if m_1 == 1 and m_2 == 3:
            score += 1
        elif m_1 == 2 and m_2 == 1:
            score += 1
        elif m_1 == 3 and m_2 == 2:
            score += 1
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
        m_1 = 0
        while m_1 not in self.allowed_attacks:
            m_1 = input('Select Attack to Use: 1 - "ROGUE", 2 - "WARRIOR", '
                        '3 - "WIZARD" :\n').lower()
            self.command(m_1)
        m_1 = int(m_1)
        m_2 = enemy_obj.select_attack()
        score = self.fight(m_1, m_2)
        if score == 0:
            print("It's a draw!\nYour lives: %s | Enemy lives: %s\n"
                  % (self.lives, enemy_obj.lives))
        elif score == 1:
            print(
                "You attacked successfully!"
            )
            self.score += score
            enemy_obj.decrease_lives(self)
        elif score == -1:
            print("You missed!\nYour lives: %s | Enemy lives: %s\n"
                  % (self.lives, enemy_obj.lives))

    def defence(self, enemy_obj):
        """
        the same as 'attack' function, but here Enemy-obj attacks and Player-obj defenses
        """
        m_1 = enemy_obj.select_attack()
        m_2 = 0
        while m_2 not in self.allowed_attacks:
            m_2 = input('Select Defence to Use: 1 - "ROGUE",'
                        ' 2 - "WARRIOR", 3 - "WIZARD"\n').lower()
            self.command(m_2)
        m_2 = int(m_2)
        score = self.fight(m_1, m_2)
        if score == 0:
            print("It's a draw!\nYour lives: %s | Enemy lives: %s\n"
                  % (self.lives, enemy_obj.lives))
        elif score == 1:
            print(
                "He hit you"
            )
            self.decrease_lives()
            print('Your lives: %s | Enemy lives: %s\n'
                  % (self.lives, enemy_obj.lives))
        elif score == -1:
            print(
                "You dodged attack!"
            )
            print('Your lives: %s | Enemy lives: %s\n'
                  % (self.lives, enemy_obj.lives))
