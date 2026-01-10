## Tuples

A _tuple_ is an **immutable** ordered sequence of items. The items of a tuple are arbitrary objects and may be of **different types**. You can use mutable objects (such as lists) as tuple items, but best practice is generally to avoid doing so.

A tuple with exactly two items is also known as a _pair_.

```python
100, 200, 300        # Tuple with three items
(3.14,)              # Tuple with one item, needs trailing comma
()                   # Empty tuple (parentheses NOT optional)
tuple('wow')         # You can also call the built-in type tuple to create a tuple
```

When using the built-in `tuple`, there's only one method, and it will create a tuple cointaining 3 items: 'w', 'o', 'w'.  `tuple` accepts only one argument. When _x_ is iterable, tuple(_x_) returns a tuple whose items are the same as those in  _x_

## Lists

A _list_ is a mutable ordered sequence of items. The items of a list are arbitrary objects and may be of different types.

```python
[42, 3.14, 'hello']  # List with three items
[100]                # List with one item
[]                   # Empty list
```

list() without arguments creates and returns an empty list, like []. When _x_ is iterable, list(_x_) returns a list whose items are the same as those in _x_

## Sets

Python has two built-in set types, set and frozenset, to represent arbitrarily ordered collections of unique items. Items in a set may be of different types, but they must all be _hashable_

Instances of type set are mutable, and thus not hashable; instances of type frozenset are immutable and hashable. You can’t have a set whose items are sets, but you can have a set (or frozenset) whose items are frozensets. Sets and frozensets are _not_ ordered.

```python
{42, 3.14, 'hello'}  # Literal for a set with three items
{100}                # Literal for a set with one item
set()                # Empty set - no literal for empty set
                     # {} is an empty dict!
```

Note that two sets or frozensets (or a set and a frozenset) may compare as equal, but since they are unordered, iterating over them can return their contents in differing order.

## dict

Library and extension modules provide other mapping types, and you can write others yourself

Keys in a dictionary may be of different types, but they must be _hashable_

```python
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

# You can unpack a dict’s contents into another dict using the ** operator
d1 = {'a':1, 'x': 0}
d2 = {'c': 2, 'x': 5}
d3 = {**d1, **d2}  # result is {'a':1, 'x': 5, 'c': 2}

# or

d4 = d1 | d2  # same result as d3

# You can also create a dictionary by calling dict.fromkeys. The first argument is an iterable whose items become the keys of the dictionary; the second argument is the value that corresponds to each and every key (all keys initially map to the same value). If you omit the second argument, it defaults to **None**

dict.fromkeys('hello', 2)    # Same as {'h':2, 'e':2, 'l':2, 'o':2}
dict.fromkeys([1, 2, 3])     # Same as {1:None, 2:None, 3:None}
```
### Alternative syntaxes

`dict(x)` can receive a list in x containing tuples will consider, for each tuple in the list, the odd value a key and the even value as a value:
```python
a = dict(x=42, y=3.14, z=7)      # Dictionary with three items, str keys  
b = dict([(1, 2), (3, 4)])       # Dictionary with two items, int keys  
c = dict([(1,'za'), ('br',23)])  # Dictionary with different key types  
d = dict()                       # Empty dictionary
```


## Iterables

## See also
[[Bytes objects#Bytearray objects]]
