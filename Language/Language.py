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
return 20 # Return statement

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
