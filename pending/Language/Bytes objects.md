A bytes object is an ordered sequence of ints from 0 to 255. bytes objects are usually encountered when reading data from or writing data to a binary source (e.g, a file, a socket, or a network resource).

A bytes object can be initialized from a list of ints or from a string of characters. A bytes literal has the same syntax as a str literal, prefixed with 'b':

```python
b'abc'
bytes([97, 98, 99])           # Same as the previous line
rb'\ = solidus'               # A raw bytes literal, containing a '\', so \ gets interpreted as a byte instead of a escape character
```

To convert a bytes object to a str, use the `bytes.decode` method. To convert a str object to a bytes object, use the `str.encode` method

## Bytearray objects
```python
ba = bytearray([97, 98, 99])  # Like bytes, can take a sequence of ints
ba[1] = 97                    # Unlike bytes, contents can be modified
print(ba.decode())            # Prints 'aac'
```
