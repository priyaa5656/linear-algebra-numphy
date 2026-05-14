# =====================================
# Math to Code Library
# Version 1
# =====================================

# user input
expr = input("Enter math expression: ")

# remove spaces
expr = expr.replace(" ", "")

# convert ^ into **
expr = expr.replace("^", "**")

# final expression
new_expr = ""

# loop through every character
for i in range(len(expr)):

    ch = expr[i]

    # check previous character
    if i > 0:
        prev = expr[i - 1]

        # number + variable
        # example: 3x -> 3*x
        if prev.isdigit() and ch.isalpha():
            new_expr += "*"

    # add character
    new_expr += ch

# output
print("\nPython Code:")
print(new_expr)