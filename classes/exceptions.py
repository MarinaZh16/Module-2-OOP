"""
module that contains exception classes and class Score
"""
import datetime


class GameOver(Exception):
    """
    class - inherited from Exception, writes score
    """
    def __init__(self, text, player):
        self.text = text
        self.player = player

    def write_score(self):
        now = datetime.datetime.today()
        rez = ('%s Player: %s; Score: %s\n' % ((now.strftime("%x")+' ' + now.strftime("%X")),
                                               self.player.name, self.player.score))
        try:
            data = Score.min_score()
            min_score = data[0]
            old_str = data[1]
            if self.player.score > min_score:
                new_str = rez
                n_f = open('score.txt', 'a')
                n_f.close()
                with open('score.txt', 'r') as file:
                    old_data = file.read()
                new_data = old_data.replace(old_str, new_str)
                with open('score.txt', 'w') as file:
                    file.write(new_data)
        except TypeError:
            with open('score.txt', 'a') as file:
                file.write(rez)


class EnemyDown(Exception):
    """
    class - inherited from Exception
    """
    pass


class RestartGame(Exception):
    """
    class - inherited from Exception, restarts game without saving score
    """
    pass


class Score(object):
    """
    score stuff
    """
    @staticmethod
    def count_lines(filename):
        """
        counts the lines in the file in which the score is recorded
        """
        with open(filename) as f:
            i = 0
            for line in f:
                i += 1
        return i

    @staticmethod
    def min_score():
        """
        check еру minimal score
        """
        if Score.count_lines('score.txt') == 10:
            line_num = []
            with open('score.txt', 'r') as file:
                for i in range(0, Score.count_lines('score.txt')):
                    line = file.readline()
                    line = line.split(':')
                    line_num.append([int(line[-1]), i])
                text = open('score.txt', 'r')
                old_str = text.readlines()[(min(line_num)[1])]
                min_score = min(line_num)[0]
            data = [min_score, old_str]
            return data
