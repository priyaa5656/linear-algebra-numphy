# 🧠 PARTIAL DERIVATIVES
👉 Partial = change with respect to one variable
👉 “Derivative” = change rate

📌 Means: If a function has two or more variables, we change one variable while keeping others constant.

## 🧠 INTUITION (REAL LIFE)
👉 Imagine you are standing on a hill ⛰️
x-direction → left-right
y-direction → forward-back
👉 The partial derivative tells you: “If I move in just one direction, what is the slope?”

## 📊 FORMULA UNDERSTANDING

👉 General:
∂f/∂x = change with respect of x , 👉 y  treat as constant 


## ✍️ PRACTICE EXAMPLES💥Rule: Differentiate with respect to one variable while treating others as constants.
###  EXAMPLE 1:

f(x, y) = x² + y²
👉 If you only change x: 👉 Treat y as a constant. 👉 Answer:  ∂f/∂x = 2x
👉 If you change only 'y': 👉 Treat 'x' as a constant.  👉 Answer:   ∂f/∂y = 2y

### Example 2:
f(x, y) = x²y + y³
👉 x ke respect me:= 2xy
👉 y ke respect me:= x² + 3y²

### Example 3:
f(x, y) = 3x² + 4xy + y²
👉 ∂f/∂x = 6x + 4y
👉 ∂f/∂y = 4x + 2y

### Example 
```python
from sympy import symbols, diff

# variables
x, y = symbols('x y')

# function
f = x**2 + y**2

# partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)

print("∂f/∂x =", df_dx)  # ∂f/∂x = 2*x
print("∂f/∂y =", df_dy) # ∂f/∂y = 2*y
```

## Machine Learning Connection

In Machine Learning:
- f(x, y) = loss function  
- x, y = parameters  
Partial derivatives help us understand:👉 how each parameter affects the output

## Key Insight

Partial Derivative = change in one direction while others remain constant