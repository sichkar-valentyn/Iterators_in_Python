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


# Implementing the task about multi-filter
def m2(x):
    return x % 2 == 0


def m3(x):
    return x % 3 == 0


def m5(x):
    return x % 5 == 0


a = [i for i in range(31)]


class multifilter:
    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_any(self, pos, neg):
        return pos >= 1

    def judge_all(self, pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for e in self.iterable:
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(e):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield e


print(list(multifilter(a, m2, m3, m5)))



