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
