import random


class NumberSet():

    def __init__(self, size):
        """NumberSet constructor"""
        self.size = size
        self.number_set = []
        self.index = 0
        for i in range(1, size + 1):
            self.number_set.append(i)

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if index >= 0 and index <= self.size - 1:
            return self.number_set[index]
        else:
            return None

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.number_set)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.index + 1 > self.size:
            return None
        else:
            self.index += 1
            return self.number_set[self.index - 1]

