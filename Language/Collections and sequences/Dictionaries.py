{1:2, 3:4, 1:5}  # The value of this dictionary is {1:5, 3:4}
{'x':42, 'y':3.14, 'z':7}    # Dictionary with three items, str keys
{1:2, 3:4}                   # Dictionary with two items, int keys
{1:'za', 'br':23}            # Dictionary with different key types
{}                           # Empty dictionary
dict()                       # Empty dictionary
# It also accepts named args or lists as arguments; also accept iterables, as long as the items in it are pairs
dict(x=42, y=3.14, z=7)      # Dictionary with three items, str keys
dict([(1, 2), (3, 4)])       # Dictionary with two items, int keys
# When you call dict and pass both a positional argument and one or more named arguments, if a key appears both in the positional argument and as a named argument, Python associates to that key the named argument’s value (i.e., the named argument “wins”)

# You can unpack a dict’s contents into another dict using the ** operator
d1 = {'a':1, 'x': 0}
d2 = {'c': 2, 'x': 5}
d3 = {**d1, **d2}  # result is {'a':1, 'x': 5, 'c': 2}
d4 = d1 | d2  # same result as d3

# You can also create a dictionary by calling dict.fromkeys. The first argument is an iterable whose items become the keys of the dictionary; the second argument is the value that corresponds to each and every key (all keys initially map to the same value). If you omit the second argument, it defaults to **None**

dict.fromkeys('hello', 2)    # Same as {'h':2, 'e':2, 'l':2, 'o':2}
dict.fromkeys([1, 2, 3])     # Same as {1:None, 2:None, 3:None}

# `dict(x)` can receive a list in x containing tuples will consider, for each tuple in the list, the odd value a key and the even value as a value:

a = dict(x=42, y=3.14, z=7)      # Dictionary with three items, str keys
b = dict([(1, 2), (3, 4)])       # Dictionary with two items, int keys
c = dict([(1,'za'), ('br',23)])  # Dictionary with different key types
d = dict()                       # Empty dictionary