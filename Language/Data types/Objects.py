## Data types

#Data values in Python are known as  _objects_; each object, aka  _value_, has a  _type_. An object that can be altered is known as a  _mutable object_, while one that cannot be altered is an  _immutable object_.

obj = 43
type(obj) # returns the type of obj
isinstance(obj, type) # check if obj is of type
isinstance(obj, int)
isinstance(obj, str)
isinstance(obj, str | int | float) # returns true if obj is any type
