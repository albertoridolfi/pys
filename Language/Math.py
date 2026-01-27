# / gives you a precise division
# - Always return a float
# - Keeps the decimal part

5 / 2      # 2.5
4 / 2      # 2.0
-5 / 2     # -2.5

# // gives you a floored division.
# - Returns the result rounded down
# - Result type: int if both operands are ints;
# - float if at least one operand is a float

5 // 2     # 2
4 // 2     # 2
5 // 2.0   # 2.0

#Important: behavior with negatives
    -5 // 2    # -3   (not -2!)

# Why? Because floor division means: “the largest integer ≤ the exact result”
# Exact result: -2.5
# Floor: -3


#If you need both floor division (`//`) and modulo (`%`) on the same operands, Python provides the  `divmod()`  function to efficiently perform the calculation, returning the two results in a tuple. Thus,  `c = divmod(a, b)`  is the same as  `c = (a // b, a % b)`.

#`round()` built into the language itself

# ⚠️ Floating-point numbers should almost never be compared for exact equality