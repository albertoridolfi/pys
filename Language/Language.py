############
# Expressions, statements, tokens and identifiers
############

# Expression: A section of code that evaluates to a single value. Can be used nearly anywhere a value is expected.

# Statement: Each line of code in Python that ends with a line break is a  _statement_
    #  - When a statement is too long to fit on a physical line, you can join two adjacent physical lines into a logical line by ensuring that the first physical line does not contain a comment and ends with a  backslash (\). More elegantly, Python also automatically joins adjacent physical lines into one logical line if an open  parenthesis ((), bracket ([), or brace ({) has not yet been closed (similar to str behavior)
    # - Physical lines after the first one in a logical line are known  as  _continuation lines_.
    # ⚠️ - Indentation rules apply to the first physical line of each logical line, not to continuation lines.

# Tokens: Python  breaks each logical line into a sequence of elementary lexical components known as  _tokens_. **Each token corresponds to a substring of the logical line**. The normal  token types are  _identifiers_,  _keywords_,  _operators_,  _delimiters_, and  _literals_.

# Identifiers

# An  _identifier_  is a name used to specify a variable, function, class, module, or other object.

# - Starts with a letter or underscore
# - Punctuation characters  such as  @,  $, and  !  are NOT ALLOWED in identifiers
#- Normal Python style is to start class names with an uppercase letter, and most other identifiers with a lowercase letter. Starting an identifier with a single leading underscore indicates by convention that the identifier is meant to be private. Starting an identifier with two leading underscores indicates a  _strongly private_identifier_; if the identifier also  _ends_  with two trailing underscores, however, this means that it’s a language-defined special name. 
# Identifiers composed of multiple words should be all lowercase with underscores between words, as in  login_password. This is sometimes referred to as  _snake case_.
# Doesn't apply to scripts, just the REPL The  identifier  _  (a single underscore) is special in interactive interpreter sessions: the interpreter binds  _  to the result of the last expression statement it has evaluated interactively, if any. This “special _” behavior is mainly for the interactive interpreter. In normal scripts (.py files), _ is just a normal variable name unless you assign to it yourself.
#- You can list reserved keywords using `keyword.kwlist`
#- In addition, Python 3.9 introduced the concept of  _soft keywords_, which are keywords that are context sensitive. That is, they are language keywords for some specific syntax constructs, but outside of those constructs they may be used as variable or function names, so they are not  _reserved_  words. No soft keywords were defined in Python 3.9, but Python 3.10 introduced the following  soft keywords: `_, case and match`. You can list them from the  keyword  module by printing  `keyword.softkwlist`

	#•	expressions (things that compute values)
	#•	statements (things that do actions)
print(21 * 2) # is not an expression, it's a statement


# Examples of expressions: 
21 * 2        # expression → evaluates to 42
"hi".upper() # expression → evaluates to "HI"
x + y        # expression

# Examples of statements:
x = 10 # Assign statement
print("hello") # Expression statement
import math  # Import statement
# return 20 # Return statement

############

# Reserved keywords
import keyword
print(keyword.kwlist)

###################
# Compound statements
###################

#	•Contains a header line ending with :
#	•Is followed by an indented block of code
#	•Groups multiple statements into a single logical unit
# Example below:

x = 10 # Simple statement
if x > 5: # Compound statement
    print("x is greater than 5")
    print("This line is also part of the if block")

########
#LOGIC
########
if True:
    pass # Do nothing. Won't work if we change here to False;
elif False:
    pass
else:
    pass

#-> Operator is → identity operator → compares the identity of the variables, rather than the value; use  `is`  _only_  for comparing directly to  `None`, and use regular comparison operators for everything else
#-> In practice, we usually say  `if spam`  or  `if not spam`, instead of directly comparing to  `True`  or  `False`
#-> The built-in type bool is a subclass of int. The only two values of type bool are `True` and `False`, which have string representations of 'True' and 'False', but also numerical values of 1 and 0, respectively

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

    # Falsy values: False, None, 0, 0.0, "", [], (), {}
    # Everything else is truthy.


    #You can use the  `not`  keyword to invert any conditional expression, such as in the following
    score = 98
    high_score = 100
    print(score != high_score)      # not equals operator, evaluates to True
    print(not score == high_score)  # not operator, evaluates to True

# You can call bool(x) with any x as the argument. The result is True when x is true and False when x is false. But it's a code smell.
# However, you  _can_  use  bool(_x_)  to count the number of true items in a sequence. For example:
def count_trues(seq):
    return sum(bool(x) for x in seq)

# for-in (instead of “for-each”)
for i in range(1, 11):
    print(i) # Prints 1,2,3,4,5,6,7,8,9,10

# Pattern matching -----------------
lunch_order = input("What would you like for lunch? ")

match lunch_order:
    case 'pizza':
        print("Pizza time!")
    case 'sandwich':
        print("Here's your sandwich")
    case 'taco':
        print('Taco, taco, TACO, tacotacotaco!')
    case _: # # The underscore (_) in the last case is the wildcard, which will match any value. This serves as a fallback case, and it must come last, as it will match anything
        print("Yummy.")

# A single case can cover multiple possible values. One way to do this is with an or pattern, where possible literal values are separated by the bar character:
match lunch_order:
    # --snip--
    case 'taco':
        print('Taco, taco, TACO, tacotacotaco!')
    case 'salad' | 'soup': # <-- ATTENTION
        print('Eating healthy, eh?')
    case _:
        print("Yummy.")


#### Null value:
None
# Functions return None as their result unless they have specific return statements coded to return other values
# None is hashable and can be used as a dict key

########### Docstrings:
def make_tea():
    """Will produce a concoction almost,
    but not entirely unlike tea.
    """
    #  ...function logic...
# Note: Docstrings are string literals, and they are seen by the interpreter; comments are ignored.
# Docstrings can be accessed like this:
make_tea.__doc__

# The  Ellipsis, written as three periods with no intervening spaces,  is a special object in Python used in numerical applications,[10](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#ch01fn29)  or as an alternative to  **None**  when  **None**  is a valid entry.

# In  Python, callable types are
# 1) those whose instances support the function call operation; and
# 2) instances of classes that supply a special method named  __call__