# Practice
## 🔥 Derivatives

### Q1: f(x) = x² + 3x  , 👉 find f'(x)
ans - 2x+3

### Q2: f(x) = x³  , 👉 find derivative
ans: 3x²

### Q3: f(x) = √x  , 👉 find derivative
ans :  1/2 x^(-1/2)
---

```python 
#Q1:
from sympy import symbols, diff
x = symbols('x')
f = x**2 + 3*x
print(diff(f, x))
```

```python 
#Q2:
from sympy import symbols, diff
x = symbols('x')
f = x**3
print(diff(f, x))
```

```python 
#Q3:
from sympy import symbols, diff
x = symbols('x')
f = x**(1/2)
print(diff(f, x))
```



## 🔵 Partial Derivative 

### Q1:f(x,y) = x² + y²  
✅ Answer:(2x, 2y)

### Q2:f(x,y) = x²y
✅ Answer:(2xy, x²)

### Q3:f(x,y) = xy²
✅ Answer:(y², 2xy)

### Q4:f(x,y) = x² + xy
✅ Answer:(2x+y, y)

### Q5:f(x,y) = x³ + y³
✅ Answer:(3x², 3y²)


```python
#Q1:
x, y = symbols('x y')
f = x**2 + y**2
print(diff(f, x))
print(diff(f, y))
```

```python
#Q2:
x, y = symbols('x y')
f = x**2 * y
print(diff(f, x))
print(diff(f, y))
```

```python
#Q3:
x, y = symbols('x y')
f = x * y**2
print(diff(f, x))
print(diff(f, y))
```

```python
#Q4:
x, y = symbols('x y')
f = x**2 + x * y
print(diff(f, x))
print(diff(f, y))
```
```python
#Q5:
x, y = symbols('x y')
f = x**3 + y**3
print(diff(f, x))
print(diff(f, y))
```
------

## 🔥 Gradient
👉 Gradient = ( ∂f/∂x , ∂f/∂y )
### Q1: f(x,y) = x² + y²  , 👉 find gradient
ans : ∂f/∂x = 2x,   ∂f/∂y = 2y ,   so gradient = ( 2x, 2y)


### Q2: f(x,y) = x² + 3y  , 👉 find gradient
ans : ∂f/∂x = 2x,   ∂f/∂y = 3 ,   so gradient = ( 2x, 3)

### Q3: f(x,y) = x³ + y²  , 👉 find gradient
ans : ∂f/∂x = 3x²,   ∂f/∂y = 2y  ,   so gradient = ( 3x², 2y)

```python 
#Q1:
from sympy import symbols, diff
x, y = symbols('x y')
f = x**2 + y**2
# Partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)
print("📊 Gradient of f(x,y) = x^2 + y^2")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)
```

```python 
#Q2:
from sympy import symbols, diff
x, y = symbols('x y')
f = x**2 + 3.y
# Partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)
print("📊 Gradient of f(x,y) = x^2 + 3y")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)
```

```python 
#Q3:
from sympy import symbols, diff
x, y = symbols('x y')
f = x**3 + y**2
# Partial derivatives
df_dx = diff(f, x)
df_dy = diff(f, y)
print("📊 Gradient of f(x,y) = x^3 + y^2")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)
```

----

## 🔥 Gradient Descent
### Q1:   f(x) = x² , start: x = 2  , lr = 0.1  ,👉 2 steps calculate karo

ans: 🔹 Step 1: 
∂f/∂x=2x,   
Gradient at x = 2 = 2x = 4
---
👉 New x Formula : x_new ​= x−α⋅(2x)  , here we choose α on our own.

x_new = 2 - 0.1×4
x_new = 1.6

🔹 Step 2:
x = 1.6
now Gradient = 2*(1.6)= 3.2
👉 New x:
x_new = 1.6 - (0.1)*(3.2)
x_new = 1.6 -0.32
x_new =1.28

🔹 Step 3:
x = 1.28
👉 Gradient = 2.56
👉 New x= 1.024

🎯 See the Pattern?
👉 x is going to bottom slowly slowly. 2 → 1.6 → 1.28 → 1.024 → … → 0


---

### Q2:  f(x) = x² + 2x ,     x = 5,     lr = 0.2

ans: 🔹 Step 1: 
∂f/∂x= 2x+2
Gradient at x = 5 = 2x+2 = 12
---
👉 New x Formula : x_new ​= x−α⋅(gradient)  , here we choose α on our own.

x_new = 5 - 0.2×12= 5-2.4
x_new = 2.6

🔹 Step 2:
x = 2.6
now Gradient = 2*(2.6)+2= 7.2
👉 New x:
x_new = 2.6 - (0.2)*(7.2)
x_new = 2.6 -1.44
x_new = 1.16


🎯 See the Pattern?
👉 x is going to bottom slowly slowly. 5 →2.6 →1.16 → … -1

---

```python 
#Q1:
x = 2
lr = 0.1

for i in range(5):
    grad = 2*x
    x = x - lr*grad
    print(x)
```

```python 
#Q2:
x = 5
lr = 0.2

for i in range(5):
    grad = 2*x+2
    x = x - lr*grad
    print(x)
   ```


summry
👉 Derivative = slope
👉 Partial = effect of one variable
👉Gradient=every effect
👉 Chain Rule = function under function
👉 Optimization = minimizing loss