import random

class Die:
    def __init__(self):
        # __init__ is called when creating an object from a class; e.g. myDie = Die() will call Die.__init__
        self.roll() # roll the die once when it is created, since it starts off with a face

    def __repr__(self):
        # the __repr__ method returns an unambiguous, printable representational string
        # of an object. the __repr__ method could be useful for debugging.
        return 'Die(' + str(self.faceValue) + ')'

    def __str__(self):
        # the __str__ method returns a human readable string representing an object.
        # __str__ can be more creative than __repr__; we'll use it to return the face.
        # __str__ vs __repr__: https://www.geeksforgeeks.org/str-vs-repr-in-python/
        return self.face

    # __init__, __repr__, and __str__ are known as "magic" methods in python.
    # more on magic methods: https://rszalski.github.io/magicmethods/

    def roll(self):
        """sets the faceValue and the face of a Die"""
        # the above is a docstring. more on docstrings: https://www.python.org/dev/peps/pep-0257/

        # https://docs.python.org/3/library/random.html#random.randint
        self.faceValue = random.randint(1, 6)

        if self.faceValue == 1:
            self.face = ' --- \n|   |\n| o |\n|   |\n --- '
        elif self.faceValue == 2:
            self.face = ' --- \n|   |\n|o o|\n|   |\n --- '
        elif self.faceValue == 3:
            self.face = ' --- \n|o o|\n| o |\n|   |\n --- '
        elif self.faceValue == 4:
            self.face = ' --- \n|o o|\n|o o|\n|   |\n --- '
        elif self.faceValue == 5:
            self.face = ' --- \n|o o|\n|o o|\n| o |\n --- '
        elif self.faceValue == 6:
            self.face = ' --- \n|o o|\n|o o|\n|o o|\n --- '
        else:
            raise Exception(self.faceValue, 'out of bounds [1, 6]')

class DiceGame:
    def __init__(self):
        """a DiceGame has two die"""
        self.die1 = Die()
        self.die2 = Die()

    def __repr__(self):
        return 'DiceGame(' + repr(self.die1) + ', ' + repr(self.die2) + ')'

    def play(self):
        self.die1.roll()
        self.die2.roll()
        print('\n'.join([
            str(self.die1),
            str(self.die2),
            'Face value: ' + str(self.die1.faceValue + self.die2.faceValue)
        ]))

# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    game = DiceGame()
    game.play()
