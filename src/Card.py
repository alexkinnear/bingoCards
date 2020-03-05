import sys

import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.idnum = idnum
        self.size = size
        self.numberSet = numberSet
        numberSet.randomize()

    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.idnum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        row = 0
        col = 0
        for i in range(self.size):
            row += 1
            for j in range(self.size):
                print("+-----", end='', file=file)
            print('+', file=file)

            for j in range(self.size):
                col += 1
                print('|', end='', file=file)
                if self.size % 2 != 0:
                    if row == self.size // 2 + 1 and j == self.size // 2:
                        print('{:^5}'.format('FREE'), end='', file=file)
                    else:
                        print('{:^5}'.format(self.numberSet.getNext()), end='', file=file)
                else:
                    print('{:^5}'.format(self.numberSet.getNext()), end='', file=file)
            print('|', file=file)

        for k in range(self.size):
            print("+-----", end='', file=file)
        print('+', file=file)
        print(file=file)





