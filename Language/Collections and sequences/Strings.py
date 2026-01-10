#Python has two built-in string types, `str` and `bytes`
#Both types are _immutable_

'A not very long string \
that spans two lines'       # Comment not allowed on previous line

'A not very long string\n\
that prints on two lines'   # You can also embed a newline in the string to make it contain two lines rather than just one

# You can wrap a literal in double quotes (`"`), single quotes (`'`), or triple quotes (`"""`) of either type.
# triple quotes (`"""`) define _multiline string literals


parrot = """
This parrot is no more!
He has ceased to be!
He's expired
  and gone to meet his maker!
He's a stiff!
Bereft of life,
he rests in peace!"""
print(parrot)

# You can start a triple-quoted literal with an escaped newline, to avoid
# having the first line of the literal string’s content at a different
# indentation level from the rest
the_text = """\
First line
Second line
""" # The same as "First line\nSecond line\n" but more readable
# Warning: """\ and """ produce different results
# The first will start WITHOUT a new line, the second will start with a new line

"""It is conventional to escape the first newline after the opening triple quotes, just to make the code look cleaner
"""

"you can _concatenate_ (combine) string literals, simply by writing them next to one another, without any operators between them"
spam = "Hello " "world" "!"

################
# RAW STRINGS
################
# `Raw strings` constitute another form of string literal, wherein the backslash (`\\`) is always treated as a literal character. They’re preceded with an `r`. _**Always use raw strings for regular expression patterns.**_
print(r"I love backslashes: \\ Aren't they cool?")
# ⚠️ If the backslash (`\\`) is the last character in your raw string, it’ll still act to escape out your closing quote and create a syntax error as a result. That has to do with Python’s own language lexing rules, not with strings

################
# F-STRINGS
################
in_stock = 0
print(f"This cheese shop has {in_stock} types of cheese.")

################
# CONCATENATING LITERALS
################
marypop = ('supercali'       # '(' begins logical line,
           'fragilistic'     # indentation is ignored
           'expialidocious') # until closing ')'
# Output:
# supercalifragilisticexpialidocious

# Multiple string literals of any kind—quoted, triple-quoted, raw, bytes, formatted—can be adjacent, with optional whitespace in between (as long as you do not mix strings containing text and bytes). The compiler concatenates such adjacent string literals into a single string object. Writing a long string literal in this way lets you present it readably across multiple physical lines and gives you an opportunity to insert comments about parts of the string

################
# ESCAPE CHARACTERS
################
#\a -> bell
#\\ -> \
#\', \"
#\n
#\r -> carriage return
#\t -> tab
#\v -> vertical tab
#\N{_name_} -> Unicode character
#\u{4 hex digits} -> Unicode character
#\U{8 hex digits}

################
# INSERTING UNICODE CHARACTERS
################
#In str literals, you can use \u followed by four hex digits, or \U followed by eight hex digits, to denote Unicode characters; you can also include the escape sequences listed in [Table 3-3](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#string_escape_sequences). str literals can also include Unicode characters using the escape sequence \N{_name_}, where _name_ is a standard [Unicode name](http://www.unicode.org/charts). For example, \N{Copyright Sign} indicates a Unicode copyright sign character (©).