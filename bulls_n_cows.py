#!/usr/bin/env python
import sys

class Game(object):
    def __init__(self, master_type, guesser_type, guess_len=4):
        try:
            self.master = master_type(guess_len)
        except TypeError:
            if guess_len == 4:
                self.master = master_type()
            else:
                raise ValueError("Master doesn't support lengths other than 4")
        try:
            self.guesser = guesser_type(guess_len)
        except TypeError:
            if guess_len == 4:
                self.guesser = guesser_type()
            else:
                raise ValueError("Master doesn't support lengths other than 4")
        self.guess_len = guess_len
        self.last_answer = None

    def __iter__(self):
        return self

    def next(self):
        if self.last_answer is None:
            guess = self.guesser.guess()
        else:
            if self.last_answer[0] == self.guess_len:
                raise StopIteration
            guess = self.guesser.guess(*self.last_answer)
        answer = self.master.check(guess)
        self.last_answer = answer
        return guess, answer

class Guesser(object):
    def __init__(self, guess_len=4):
        self.guess_len = guess_len

    def guess(self, bulls=None, cows=None):
        raise NotImplementedError

class Master(object):
    def __init__(self, guess_len=4):
        self.guess_len = guess_len

    def check(self, guess):
        raise NotImplementedError

def load_class(cls_path):
    module_name, class_name = cls_path.rsplit('.', 1)
    __import__(module_name)
    module = sys.modules[module_name]
    return getattr(module, class_name)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print >>sys.stderr, \
                 "Syntax: bulls_n_cows.py module.MasterType module.GuesserType"
        sys.exit(1)

    master_type = load_class(sys.argv[1])
    guesser_type = load_class(sys.argv[2])
    game = Game(master_type, guesser_type)
    for guess, (bulls, cows) in game:
        print "Guess: %s Bulls: %s Cows: %s" % (guess, bulls, cows)
