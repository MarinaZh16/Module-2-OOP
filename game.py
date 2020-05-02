"""
module with 'Rock-paper-scissors'-based game
"""

from module2.classes import models, exceptions


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
        player = models.Player(name)
        enemy = models.Enemy()
        start = 0
        while start != player.allowed_commands[0]:
            start = input('Enter "start" to START game\n').lower()
        print(
            'Enter "HELP", to watch allowed commands'
        )
        while True:
            try:
                player.attack(enemy)
            except exceptions.EnemyDown:
                enemy.level += 1
                enemy.lives = enemy.level
                player.score += 5
                player.level += 1
                print('-'
                      * 65)
                print('You killed enemy! Your Score: %s. Level: %s' % (player.score,
                                                                       player.level))
                print('-'
                      * 65)
            else:
                print('Your lives: %s | Enemy lives: %s'
                      % (player.lives, enemy.lives))
                player.defence(enemy)
                print('Your lives: %s | Enemy lives: %s'
                      % (player.lives, enemy.lives))
    except exceptions.RestartGame:
        print(
            "You reloaded game! Your score wasn't save"
        )
        play()


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    except exceptions.GameOver as game_over:
        game_over.write_score()
        print(game_over.text)
    finally:
        print(
            "Good Bye!"
        )
