# File: iterators.py
# Description: Examples on how to use iterators in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to use iterators in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichhttps://github.com/sichkar-valentyn/Iterators_in_Python (date of access: XX.XX.XXXX)


# Showing the standard way how to iterate
# And explaining how it is done in Python

# Creating list and dictionary for the experiments
lst = [1, 2, 3, 4, 5]
book = {'title': 'Python', 'author': 'Goodboy', 'year': 2018}


# Standard way how to iterate
for i in lst:
    print(i)

for i in book:
    print(i)

# Another way which describes how it is done inside Python
it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
