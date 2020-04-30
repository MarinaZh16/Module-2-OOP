"""
module with 'Rock-paper-scissors'-based game
"""

from module2.classes import models, exceptions
P = models.Player
E = models.Enemy
GAME_OVER = exceptions.GameOver
RESTART = exceptions.RestartGame


def play():
    """
    function that launches the game
    """
    try:
        print(
            'Welcome to the Game!'
        )
        name = input('Wat is your name?\n').capitalize()
        print(
            "Hello, %s!" % name
        )
        player = P(name)
        enemy = E()
        start = 0
        while start != player.allowed_commands[0]:
            start = input('Enter "start" to START game\n').lower()
        print(
            'Enter "HELP", to watch allowed commands'
        )
        while True:
            player.attack(enemy)
            if enemy.lives != 0:
                player.defence(enemy)
            else:
                enemy.lives = enemy.level
    except RESTART:
        print(
            "You reloaded game! Your score wasn't save"
        )
        play()


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    except GAME_OVER as game_over:
        print(game_over.text)
    finally:
        print(
            "Good Bye!"
        )
