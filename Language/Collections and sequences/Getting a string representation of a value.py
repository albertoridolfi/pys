x = None

str(x) # returns the _human-readable_ representation of the value
repr(x) #: _canonical string representation_ of the value: that is, (usually) the value as Python sees it. In the case of many basic data types, this will return the same thing as `str()`, but when used on most objects, the output contains additional information useful in debugging