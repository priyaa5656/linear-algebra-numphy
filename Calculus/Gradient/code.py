# 🧠 GRADIENT + GRADIENT DESCENT DEMO

from sympy import symbols, diff

# -----------------------------
# ✅ 1. Gradient Calculation
# -----------------------------
x, y = symbols('x y')

# Function: f(x, y) = x^2 + y^2
f = x**2 + y**2

# Partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)

print("📊 Gradient of f(x,y) = x^2 + y^2")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)

# Value at (1,2)
val_x = 1
val_y = 2

print("\n📍 Gradient at (1,2):")
print("(", df_dx.subs({x: val_x, y: val_y}), ",",
           df_dy.subs({x: val_x, y: val_y}), ")")

# -----------------------------
# ✅ 2. Gradient Descent (Manual)
# -----------------------------

print("\n🚀 Gradient Descent on f(x) = x^2")

# initial value
x_val = 4
learning_rate = 0.1

for i in range(10):
    grad = 2 * x_val   # derivative of x^2
    x_val = x_val - learning_rate * grad

    print(f"Step {i+1}: x = {round(x_val, 4)}")

# -----------------------------
# ✅ 3. Final Understanding
# -----------------------------

print("\n💡 Final Insight:")
print("Gradient → direction of increase")
print("-Gradient → direction of decrease (used in ML)")
print("Goal → reach minimum loss 🎯")