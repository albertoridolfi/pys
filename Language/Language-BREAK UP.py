If you need both floor division (`//`) and modulo (`%`) on the same operands, Python provides the  `divmod()`  function to efficiently perform the calculation, returning the two results in a tuple. Thus,  `c = divmod(a, b)`  is the same as  `c = (a // b, a % b)`.

`round()` built into the language itself

# Logic

- `if`, `elif`, `else`
- `True`, `False`
- `None` (`NoneType`)
- Operator `is` → identity operator → compares the identity of the variables, rather than the value; use  `is`  _only_  for comparing directly to  `None`, and use regular comparison operators for everything else.
- n practice, we usually say  `if spam`  or  `if not spam`, instead of directly comparing to  `True`  or  `False`
    ```python
    spam = True
    eggs = False
    potatoes = None
    
    if spam is True:          # Evaluates to True
        print("We have spam.")
    
    if spam is not False:     # Evaluates to True
        print("I DON'T LIKE SPAM!")
    
    if spam:                  # Implicitly evaluates to True (preferred)
        print("Spam, spam, spam, spam...")
    
    if eggs is False:         # Evaluates to True
        print("We're all out of eggs.")
    
    if eggs is not True:      # Evaluates to True
        print("No eggs, but we have spam, spam, spam, spam...")
    
    if not eggs:              # Implicitly evaluates to True (preferred)
        print("Would you like spam instead?")
    
    if potatoes is not None:  # Evaluates to False (preferred)
        print("Yum")          # We never reach this...potatoes is None!
    
    if potatoes is None:      # Evaluates to True (preferred)
        print("Yes, we have no potatoes.")
    
    if eggs is spam:          # Evaluates to False (CAUTION!!!)
        print("This won't work.")
    ```
    
    - The  None  constant, values representing zero, and empty collections are all considered “falsey,” while most other values are “truthy.
    - `and`, `or`, `not`
    - You can use the  `not`  keyword to invert any conditional expression, such as in the following
        ```python
        score = 98
        high_score = 100
        print(score != high_score)      # not equals operator, evaluates to True
        print(not score == high_score)  # not operator, evaluates to True
        ```
        
    - Walrus operator (`:=`) → _assignment expressions → assign a value to a variable and use that variable in another expression at the same time → makes var available in the outer scope
        ```python
        if (eggs := 7 + 5) == 12:
            print("We have one dozen eggs")
        
        print(eggs)  # prints 12
        ```

- Any nonzero number or nonempty container (e.g., string, tuple, list, set, or dictionary) is true
- Zero (0, of any numeric type),  `None`, and empty containers are false
- ⚠️ Floating-point numbers should almost never be compared for exact equality
- The built-in type bool is a subclass of int. The only two values of type bool are True and False, which have string representations of 'True' and 'False', but also numerical values of 1 and 0, respectively. 
- You can call bool(x) with any x as the argument. The result is True when x is true and False when x is false. But it's a code smell. However, you  _can_  use  bool(_x_)  to count the number of true items in a sequence. For example:

```python
def count_trues(seq):
    return sum(bool(x) for x in seq)
```

# Loops

```python
# for-in (instead of “for-each”)
for i in range(1, 11):
    print(i) # Prints 1,2,3,4,5,6,7,8,9,10
```

# Pattern matching

```python
lunch_order = input("What would you like for lunch? ")

match lunch_order:
    case 'pizza':
        print("Pizza time!")
    case 'sandwich':
        print("Here's your sandwich")
    case 'taco':
        print('Taco, taco, TACO, tacotacotaco!')
    case _:
        print("Yummy.")

# The underscore (_) in the last case is the wildcard, which will match any value. This serves as a fallback case, and it must come last, as it will match anything

##########################################
# A single case can cover multiple possible values. One way to do this is with an or pattern, where possible literal values are separated by the bar character: 
match lunch_order:
    # --snip--
    case 'taco':
        print('Taco, taco, TACO, tacotacotaco!')
    case 'salad' | 'soup': # <<<<<<<<
        print('Eating healthy, eh?')
    case _:
        print("Yummy.")
```

---

# Etc

```python
# Doing nothing
pass

# Null value
None # has no methods or other attributes
# Functions return None as their result unless they have specific return statements coded to return other values
# None is hashable and can be used as a dict key

###############################################################

# Comments:
# Like this

# Docstrings:
def make_tea():
    """Will produce a concoction almost,
    but not entirely unlike tea.
    """
    #  ...function logic...
# Note: Docstrings are string literals, and they are seen by the interpreter; comments are ignored.

# Docstrings can be accessed like this:
make_tea.__doc__

###############################################################

... # The  Ellipsis, written as three periods with no intervening spaces,  is a special object in Python used in numerical applications,[10](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#ch01fn29)  or as an alternative to  **None**  when  **None**  is a valid entry.
###############################################################
# In  Python, callable types are those whose instances support the function call operation, and instances of classes that supply a special method named  __call__
```