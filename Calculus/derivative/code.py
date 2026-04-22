# =========================
# DERIVATIVES + ML FUNCTIONS
# =========================

from sympy import symbols, diff, exp

# variable
x = symbols('x')

# -------------------------
# BASIC DERIVATIVE
# -------------------------
print("=== BASIC DERIVATIVE ===")
f = x**2
print("f(x) =", f)
print("f'(x) =", diff(f, x))   # 2x
print()


# -------------------------
# POWER RULE
# -------------------------
print("=== POWER RULE ===")
f1 = x**3
print("f(x) =", f1)
print("f'(x) =", diff(f1, x))   # 3x^2
print()


# -------------------------
# CONSTANT RULE
# -------------------------
print("=== CONSTANT RULE ===")
f2 = 5
print("f(x) =", f2)
print("f'(x) = 0")   # constant ka derivative 0
print()


# -------------------------
# CONSTANT MULTIPLE RULE
# -------------------------
print("=== CONSTANT MULTIPLE RULE ===")
f3 = 5*x**2
print("f(x) =", f3)
print("f'(x) =", diff(f3, x))   # 10x
print()


# -------------------------
# SUM RULE
# -------------------------
print("=== SUM RULE ===")
f4 = x**2 + 3*x
print("f(x) =", f4)
print("f'(x) =", diff(f4, x))   # 2x + 3
print()


# -------------------------
# PRODUCT RULE
# -------------------------
print("=== PRODUCT RULE ===")
f5 = x**2 * (x + 1)
print("f(x) =", f5)
print("f'(x) =", diff(f5, x))   # 3x^2 + 2x
print()


# -------------------------
# CHAIN RULE
# -------------------------
print("=== CHAIN RULE ===")
f6 = (x**2 + 1)**3
print("f(x) =", f6)
print("f'(x) =", diff(f6, x))   # 6x(x^2 + 1)^2
print()


# =========================
# ML FUNCTIONS
# =========================

# -------------------------
# SIGMOID
# -------------------------
print("=== SIGMOID ===")
sigmoid = 1 / (1 + exp(-x))
print("sigmoid(x) =", sigmoid)
print("sigmoid'(x) =", diff(sigmoid, x))
print()


# -------------------------
# RELU
# -------------------------
print("=== RELU ===")
print("ReLU derivative:")
print("x > 0  → 1")
print("x <= 0 → 0")
print()


# -------------------------
# TANH
# -------------------------
print("=== TANH ===")
tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
print("tanh(x) =", tanh)
print("tanh'(x) =", diff(tanh, x))
print()


# =========================
# VALUE AT POINT
# =========================
print("=== VALUE AT x = 2 ===")
value = diff(x**2, x).subs(x, 2)
print("f'(2) =", value)   # 4
print()