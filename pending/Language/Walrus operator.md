
An _assignment_ is a simple statement that assigns values to variables, as we discuss in [“Assignment Statements”](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#assignment_statements). An assignment in Python using the = operator is a statement and can never be part of an expression. To perform an assignment as part of an expression, you must use the := (known as the “walrus”) operator. You’ll see some examples of using := in [“Assignment Expressions”](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#assignment_expressions).


## Examples
```python
walrus = 0  
val2 = (walrus = True) # ERROR  
print(walrus)  
print(val2)
#################################
walrus = 0  
val2 = (walrus := True)  
print(walrus)  
print(val2)
```


https://realpython.com/python-walrus-operator/