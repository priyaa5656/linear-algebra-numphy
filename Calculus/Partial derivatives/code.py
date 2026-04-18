# =========================
# PARTIAL DERIVATIVES - PRACTICE
# =========================

from sympy import symbols, diff

# variables
x, y = symbols('x y')

# -------------------------
# Example 1
# f(x, y) = x^2 + y^2
# -------------------------
print("=== Example 1 ===")
f1 = x**2 + y**2

df1_dx = diff(f1, x)
df1_dy = diff(f1, y)

print("f(x,y) =", f1)
print("∂f/∂x =", df1_dx)   # 2x
print("∂f/∂y =", df1_dy)   # 2y
print()


# -------------------------
# Example 2
# f(x, y) = x^2*y + y^3
# -------------------------
print("=== Example 2 ===")
f2 = x**2 * y + y**3

df2_dx = diff(f2, x)
df2_dy = diff(f2, y)

print("f(x,y) =", f2)
print("∂f/∂x =", df2_dx)   # 2xy
print("∂f/∂y =", df2_dy)   # x^2 + 3y^2
print()


# -------------------------
# Example 3
# f(x, y) = 3x^2 + 4xy + y^2
# -------------------------
print("=== Example 3 ===")
f3 = 3*x**2 + 4*x*y + y**2

df3_dx = diff(f3, x)
df3_dy = diff(f3, y)

print("f(x,y) =", f3)
print("∂f/∂x =", df3_dx)   # 6x + 4y
print("∂f/∂y =", df3_dy)   # 4x + 2y
print()


# =========================
# BONUS: USER PRACTICE
# =========================

print("=== Try Yourself ===")

# Example: f(x,y) = x*y + y^3
f4 = x*y + y**3

print("Function:", f4)
print("∂f/∂x =", diff(f4, x))   # y
print("∂f/∂y =", diff(f4, y))   # x + 3y^2