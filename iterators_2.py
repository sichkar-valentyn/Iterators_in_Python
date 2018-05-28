# File: iterators_2.py
# Description: Examples on how to use iterators in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to use iterators in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichhttps://github.com/sichkar-valentyn/Iterators_in_Python (date of access: XX.XX.XXXX)


from random import random


# Creating the class for iterations
class RandomIterator:
    # We add the method __iter__ if we want to iterate this class
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


# Instance of the class
# But we can say that x is iterator if it has method next
x = RandomIterator(3)

print(next(x))
print(next(x))
print(next(x))


# Iterating the class
for x in RandomIterator(3):
    print(x)
