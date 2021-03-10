""" Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])

Sort this list by using the sorted() build in function.

Sort the list in reversed order.

Sort the list on the lenght of the name.

Sort the list based on the last letter in the name.

Sort the list with the names where the letter ‘a’ is in the name first. """

names = ['Izaura', 'Genowfa', 'Bogdan', 'Arnold', 'Gniewomir', 'Bob', "aron"]

print(sorted(names))
print(sorted(names, reverse=True))
print(sorted(names, key=len))

##Sorted by last letter in string
def by_last(s):
    return s[-1]

print(sorted(names, key=by_last))

##Sorted by nams with a (strange stuff)
def a_first(s):
    if s[0] == 'a':
        return False
    return True

print(sorted(names, key=a_first))