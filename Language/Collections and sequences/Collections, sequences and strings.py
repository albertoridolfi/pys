#########################
#SEQUENCES (Lists [], dictionaries{}, sets{}, tuples,())
#########################
#-> Lists ---------
# MUTABLE
# ORDERED
# ITENS CAN BE DIFFERENT TYPES
cheeses = ["Red Leicester", "Tilsit", "Caerphilly", "Bel Paese"]
[42, 3.14, 'hello']  # List with three items
[100]                # List with one item
[]                   # Empty list
list()               # Empty list

#-> Tuples ---------
# IMMUTABLE
# ORDERED
# ITENS CAN BE DIFFERENT TYPES
# MUTABLE ITEMS CAN BE USED (CODE SMELL)
answers = ("Sir Lancelot", "To seek the holy grail", 0x0000FF)
print(answers[0])  # prints "Sir Lancelot"
# answers[0] = "King Arthur"  # raises TypeError BECAUSE Tuples, unlike lists, are IMMUTABLE.
#A tuple with exactly two items is also known as a _pair_.

100, 200, 300        # Tuple with three items
(3.14,)              # Tuple with one item, needs trailing comma
()                   # Empty tuple (parentheses NOT optional)
tuple('wow')         # You can also call the built-in type tuple to create a tuple
                     # Result: (w, o, w)

#->Dictionaries ---------
d = {
    "name": "Alice",
    "age": 30,
    "is_admin": False
}
# (see specific page for more info)

#->Sets ---------
# NOT ORDERED
# Items can be different types, but they must be hashable
# TWO SUBTYPES: SET AND FROZENSET
    # SET
        # MUTABLE
        # NOT HASHABLE
        # CAN'T HAVE SETS INSIDE AS ITEMS
    # FROZENSET
        # IMMUTABLE
        # HASHABLE
        # CAN HAVE SETS INSIDE AS ITEMS
{42, 3.14, 'hello'}  # Literal for a set with three items
{100}                # Literal for a set with one item
set()                # Empty set - no literal for empty set
{} # ⚠️is an empty dict!

# Note that two sets or frozensets (or a set and a frozenset) may compare as equal, but since they are unordered, iterating over them can return their contents in differing order.
#########################


# Applies to tuples and lists:
# # When _x_ is iterable, `tuple(_x_)` returns a tuple whose items are the same as those in  _x_