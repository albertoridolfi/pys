# # Bytes objects: orderered sequenec of ints from 0 to 255
# usually encountered when reading data from or writing data to a binary source (e.g, a file, a socket, or a network resource)

# A bytes object can be initialized from a list of ints or from a string of characters. A bytes literal has the same syntax as a str literal, prefixed with 'b':

b'abc'
bytes([97, 98, 99])           # Same as the previous line
rb'\ = solidus'               # A raw bytes literal, containing a '\', so \ gets interpreted as a byte instead of a escape character

# Convert bytes objects -> str:
bytes.decode(b'abc')          
# Convert str -> bytes obj:
str.encode('abc')

## Bytearray objects
# - mutable 
# - ordered 
# - sequence of ints from 0 to 255
ba = bytearray([97, 98, 99])  # Like bytes, can take a sequence of ints
#ba = bytearray([97, 98, 99, 500])  # Will give an error because 500 is out of range
ba[1] = 97                    # Unlike bytes, contents can be modified
print(ba.decode())            # Prints 'aac'

