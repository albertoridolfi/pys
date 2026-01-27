
#An _assignment_ is a simple statement that assigns values to variables, as we discuss in [“Assignment Statements”](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#assignment_statements). An assignment in Python using the = operator is a statement and can never be part of an expression. To perform an assignment as part of an expression, you must use the := (known as the “walrus”) operator. You’ll see some examples of using := in [“Assignment Expressions”](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch03.html#assignment_expressions).
# Another explanation: Walrus operator (`:=`) → _assignment expressions → assign a value to a variable and use that variable in another expression at the same time → makes var available in the outer scope

walrus = 0  
val2 = (walrus = True) # ERROR  
print(walrus)  
print(val2)
#################################
walrus = 0  
val2 = (walrus := True)  
print(walrus)  
print(val2)

# See also https://realpython.com/python-walrus-operator/


if (eggs := 7 + 5) == 12:
    print("We have one dozen eggs")

print(eggs)  # prints 12