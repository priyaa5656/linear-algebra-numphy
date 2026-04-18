# =========================
# DERIVATIVE - PRACTICE
# =========================

from sympy import symbols, diff

# variable
x = symbols('x')

# -------------------------
# Example 1: f(x) = x^2
# -------------------------
print("=== Example 1 ===")
f1 = x**2
df1 = diff(f1, x)

print("f(x) =", f1)
print("f'(x) =", df1)   # 2x
print()


# -------------------------
# Example 2: f(x) = x^3
# -------------------------
print("=== Example 2 ===")
f2 = x**3
df2 = diff(f2, x)

print("f(x) =", f2)
print("f'(x) =", df2)   # 3x^2
print()


# -------------------------
# Example 3: f(x) = x^2 + 3x
# -------------------------
print("=== Example 3 ===")
f3 = x**2 + 3*x
df3 = diff(f3, x)

print("f(x) =", f3)
print("f'(x) =", df3)   # 2x + 3
print()


# -------------------------
# Value at a specific point
# -------------------------
print("=== Value at x = 2 ===")
value = df1.subs(x, 2)

print("f'(2) =", value)   # 4
print()


# -------------------------
# Practice Section
# -------------------------
print("=== Practice ===")

f4 = x**4
print("f(x) =", f4)
print("f'(x) =", diff(f4, x))   # 4x^3
print()

f5 = 2*x**2 + 5
print("f(x) =", f5)
print("f'(x) =", diff(f5, x))   # 4x
print()

f6 = x**3 + 2*x
print("f(x) =", f6)
print("f'(x) =", diff(f6, x))   # 3x^2 + 2
print()