- Each line of code in Python that ends with a line break is a _**statement**._ A section of code that evaluates to a single value is called an _**expression**. You can put expressions nearly anywhere a value is expected._
- If you ever need to place multiple statements on the same line, you can separate them with a semicolon (;) ⚠️ bad practice
- PEP8 convention: 4 spaces
- Python is considered a _strongly typed language_, meaning you usually can’t magically combine data of different types
- Python is, however, _weakly bound_, so it is possible to assign a value of a different type to an existing variable
- When a statement is too long to fit on a physical line, you can join two adjacent physical lines into a logical line by ensuring that the first physical line does not contain a comment and ends with a backslash (\). More elegantly, Python also automatically joins adjacent physical lines into one logical line if an open parenthesis ((), bracket ([), or brace ({) has not yet been closed
- Triple-quoted string literals can also span physical lines.
- Physical lines after the first one in a logical line are known as _continuation lines_.
- Indentation rules apply to the first physical line of each logical line, not to continuation lines.
- ⚠️ Standard Python style is to use four spaces (_never_ tabs) per indentation level. If you must use tabs, Python does not allow mixing tabs and spaces for indentation. Configure your favorite editor to expand a Tab keypress to four spaces
--------------
# Tokens
Python breaks each logical line into a sequence of elementary lexical components known as _tokens_. Each token corresponds to a substring of the logical line. The normal token types are _identifiers_, _keywords_, _operators_, _delimiters_, and _literals_, which we cover in the following sections.

## Identifiers
An _identifier_ is a name used to specify a variable, function, class, module, or other object.
- Starts with a letter or underscore
- Punctuation characters such as @, $, and ! are not allowed in identifiers
- Normal Python style is to start class names with an uppercase letter, and most other identifiers with a lowercase letter. Starting an identifier with a single leading underscore indicates by convention that the identifier is meant to be private. Starting an identifier with two leading underscores indicates a _strongly private_identifier; if the identifier also _ends_ with two trailing underscores, however, this means that it’s a language-defined special name. Identifiers composed of multiple words should be all lowercase with underscores between words, as in login_password. This is sometimes referred to as _snake case_.
- The identifier **_** (a single underscore) is special in interactive interpreter sessions: the interpreter binds **_** to the result of the last expression statement it has evaluated interactively, if any.
- You can list reserved keywords using `keyword.kwlist`
- In addition, Python 3.9 introduced the concept of _soft keywords_, which are keywords that are context sensitive. That is, they are language keywords for some specific syntax constructs, but outside of those constructs they may be used as variable or function names, so they are not _reserved_ words. No soft keywords were defined in Python 3.9, but Python 3.10 introduced the following soft keywords: `_, case and match`. You can list them from the keyword module by printing `keyword.softkwlist`

### Unicode normalization ⚠️
```python
a, o = 100, 101
ª, º = 200, 201
# 200 201 200 201  # expected "100 101 200 201"
# It is best to avoid using normalizable Unicode characters in your Python identifiers
```


## Data types

Data values in Python are known as _objects_; each object, aka _value_, has a _type_. An object that can be altered is known as a _mutable object_, while one that cannot be altered is an _immutable object_.

```python
type(obj) # returns the type of obj
isinstance(obj, type) # check if obj is of type
isinstance(obj, tuple_of_types)
isinstance(obj, type1 | type2 | type3) # returns true if obj is any type
```

```

## Delimiters
```python
[42, 3.14, 'hello']     # List
[]                      # Empty list
100, 200, 300           # Tuple
(100, 200, 300)         # Tuple
()                      # Empty tuple
{'x':42, 'y':3.14}      # Dictionary
{}                      # Empty dictionary
{1, 2, 4, 8, 'string'}  # Set
# There is no literal form to denote an empty set; use set() instead
```

Note: a block of code can be called a "compound statement"

----------------------

# Numbers

```python
1, 23, 3493                    # Decimal integer literals
0b010101, 0b110010, 0B01       # Binary integer literals
0o1, 0o27, 0o6645, 0O777       # Octal integer literals
0x1, 0x17, 0xDA5, 0xda5, 0Xff  # Hexadecimal integer literals
111_111, 1_111, 11111_1, 11_11_11 # Underscores as visual separators, have no meaning to the interpreter
0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0E0  # Floating-point literals

2.5.as_integer_ratio() # result: tuple (5, 2)

2.5.is_integer() # returns False

```
`Decimal` stores fixed-point decimal numbers, while `Fraction` does the same for fractions. To use either, you’ll need to import them first

```python
from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)  # 1/3
print(third_fixed)     # 0.333
print(third_float)     # 0.3333333333333333

third_float = float(third_fraction)
print(third_float)     # 0.3333333333333333

third_float = float(third_fixed)
print(third_float)     # 0.333
```

```python
print(-42)         # negative (unary), evaluates to -42
print(abs(-42))    # absolute value, evaluates to 42
print(40 + 2)      # addition, evaluates to 42
print(44 - 2)      # subtraction, evaluates to 42
print(21 * 2)      # multiplication, evaluates to 42
print(680 / 16)    # division, evaluates to 42.5
print(680 // 16)   # floor division (discard remainder), evaluates to 42
print(1234 % 149)  # modulo, evaluates to 42
print(7 ** 2)      # exponent, evaluates to 49
print((9 + 5) * 3) # parentheses, evaluates to 42
```

If you need both floor division (`//`) and modulo (`%`) on the same operands, Python provides the `divmod()` function to efficiently perform the calculation, returning the two results in a tuple. Thus, `c = divmod(a, b)` is the same as `c = (a // b, a % b)`.

`round()` built into the language itself

# Logic

- `if`, `elif`, `else`
- `True`, `False`
- `None` (`NoneType`)
- Operator `is` → identity operator → compares the identity of the variables, rather than the value; use `is` _only_ for comparing directly to `None`, and use regular comparison operators for everything else.
- n practice, we usually say `if spam` or `if not spam`, instead of directly comparing to `True` or `False`
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
    
    - The None constant, values representing zero, and empty collections are all considered “falsey,” while most other values are “truthy.
    - `and`, `or`, `not`
    - You can use the `not` keyword to invert any conditional expression, such as in the following
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
- Zero (0, of any numeric type), `None`, and empty containers are false
- ⚠️ Floating-point numbers should almost never be compared for exact equality
- The built-in type bool is a subclass of int. The only two values of type bool are True and False, which have string representations of 'True' and 'False', but also numerical values of 1 and 0, respectively. 
- You can call bool(x) with any x as the argument. The result is True when x is true and False when x is false. But it's a code smell. However, you _can_ use bool(_x_) to count the number of true items in a sequence. For example:

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

... # The Ellipsis, written as three periods with no intervening spaces, is a special object in Python used in numerical applications,[10](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#ch01fn29) or as an alternative to **None** when **None** is a valid entry.
###############################################################
# In Python, callable types are those whose instances support the function call operation, and instances of classes that supply a special method named __call__
```