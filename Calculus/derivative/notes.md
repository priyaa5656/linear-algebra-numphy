# 🧠 DERIVATIVE 
👉 Derivative = Rate of change
👉 Meaning:➡️ “How fast the function is changing as x changes”

## 📌 2. Real-Life Intuition: 👉 Imagine you are driving a car 🚗
Position = Where you are located ,  Speed ​​= How fast you are moving
👉 Speed ​​= The derivative of position



## 📌 3. Average vs. Instant Change
🟡 Average Change 👉 Between two points:
   f(b)−f(a)
----------------       👉 Example: The change from 1 to 2
     b-a 

## 🔴 Instant Change (Derivative)
👉 The change at one exact point
👉 This is precisely what a derivative is! 🔥

## 📊 4. Formula (Core Idea)
f′(x)= limh→0 f(x+h)−f(x)
​               ------------
                    h
​
### 💡 Meaning 
👉 Introduce a small change (h) in x
👉 Observe the difference in the output
👉 h → 0 (becomes extremely small)
👉 You obtain the exact slope 🎯


## Example 1:
### 📌 Step 1: Understanding the Problem
👉 Suppose we have a function: f(x) = x²
👉 Question: ➡️ “How fast does the output change as x changes?”

### 📌 Step 2: Average Change (Starting Point)
👉 Let's take two points:
   x = 2  ,       x = 3
 f(2) = 4 ,  👉 f(3) = 9

👉 Change:(9 - 4) / (3 - 2) = 5  👉 This represents the average change.

### 📌 Step 3: The Real Problem
👉 What we actually want is:➡️ “What is the exact change at x = 2?”
👉 But here is the problem: How do we calculate the slope at a single point? 🤯

### 📌 Step 4: The Trick (VERY IMPORTANT 🔥)
👉 Let's consider a small change near x = 2:   x + h
👉 The new point:   f(2 + h)

### 📌 Step 5: 📊 Final Formula (The Derivative)
f′(x)=lim h→0 hf(x+h)−f(x)
​              ------------
                   h

### 📌 Step 6: Applying it to f(x) = x²
👉 f(x+h): = (x + h)² = x² + 2xh + h²
👉 Substitute into the formula:  (x² + 2xh + h² - x²) / h =  (2xh + h²) / h  = 2x + h
👉 Now, let h → 0   👉 Final Answer:👉 2x 🎯
💥 Final Meaning 👉 f'(x) = 2x means ➡️ all point slope = 2x

```python 
from sympy import symbols, diff
f = x²
x = symbols('x')
print(diff(f, x)) # 2x
```
## 🔥 6. Shortcut Rule (MOST IMPORTANT) 👉 xⁿ → n·xⁿ⁻¹
✍️ Examples
x² → 2x
x³ → 3x²
5x → 5
x² + 3x → 2x + 3


# understand
👉 You are standing on a hill ⛰️
Flat ground → Slope = 0
Climbing up → Slope is positive
Going down → Slope is negative
👉 The Derivative tells you the slope

🧠 So, why do we need rules?
👉 Using the limit formula every single time is a no-go ❌ (it's too lengthy).
👉 That is why shortcut rules were created ✔️.


## Common Derivative Rules

### 1️⃣ Power Rule :  
If f(x) = xⁿ, then f'(x) = nxⁿ⁻¹
Example : f(x) = x²
Using power rule: f'(x) = 2x^(2-1) = 2x¹ = 2x
Verification: f'(x) = 2x
👉 Just bring the power down and subtract 1

f1 = x   **3
```python
print("f(x) =", f1)
print("f'(x) =", diff(f1, x))   # 3x^2
print()
```

### 2️⃣ Constant Rule:
✔️ Constant Rule:
👉 f(x) = c → f'(x) = 0
✔️ Constant Multiple Rule:
👉 f(x) = c·g(x) → f'(x) = c·g'(x)
👉  derivative of number = 0
Example:
5 → 0
10 → 0
👉 Because it's just not changing.

```python
f2 = 5*x**2
print("f(x) =", f2)
print("f'(x) =", diff(f2, x))   # 10x
print()
```

### 3️⃣ Sum Rule:
👉👉 Find separate derivatives, then add them
Example:  x² + 3x 👉 = (2x) + (3) 
👉 answer:               2x + 3

f3 = x + 3*x
```python
print("f(x) =", f3)
print("f'(x) =", diff(f3, x))   # 2x + 3
print()
```


### 4️⃣ Product Rule (IMPORTANT)
If f(x) = g(x)·h(x), then f'(x) = g'(x)·h(x) + g(x)·h'(x)
👉 When multiplying:👉 Don't memorize the formula just yet. 👉 Just understand the pattern:
👉 (first × second)' = first'×second + first×second'
Example:
x² (x+1)
👉 = (2x)(x+1) + (x²)(1)
👉 = 2x² + 2x + x²
👉 = 3x² + 2x

```python
f4 = x**2 * (x + 1)
print("f(x) =", f4)
print("f'(x) =", diff(f4, x))   # 3x^2 + 2x
print()
```



### 5️⃣ Chain Rule (MOST IMPORTANT 🔥)
👉 “Outer ka derivative × Inner ka derivative”
If f(x) = g(h(x)), then f'(x) = g'(h(x))·h'(x)
👉 When there is a function within a function
Example:
f(x) = (x² + 1)³
👉 outer = power ,  👉 inner = x² + 1
👉 step:
power rule: 3( )²
inner ka derivative: 2x
h'(x) = 2x 
g'(u) = 3u² 
👉 final:
f'(x) = g'(h(x))·h'(x)
f'(x) = 3(h(x))²·(2x)
f'(x) = 3(x² + 1)²·(2x)
f'(x) = 6x(x² + 1)²

```python
f5 = (x**2 + 1)**3
print("f(x) =", f5)
print("f'(x) =", diff(f5, x))   # 6x(x^2 + 1)^2
print()
```


## derivatives you'll encounter in neural networks:

Function	Derivative	Notes
Power Functions		
f(x) = c (constant)	              | f'(x) = 0	                       |   Constant rule
f(x) = x	                          | f'(x) = 1	                       |Identity function
f(x) = x²	                       |f'(x) = 2x	                       | Power rule
f(x) = x³	                       |f'(x) = 3x²	                       |Power rule
f(x) = xⁿ	                       |f'(x) = nxⁿ⁻¹	                    |General power rule
f(x) = √x = x^(1/2)	              |f'(x) = 1/(2√x)	                 |Square root
f(x) = 1/x = x^(-1)                |f'(x) = -1/x²	                    |Reciprocal
## Exponential & Logarithmic		
f(x) = eˣ	                       |f'(x) = eˣ	                       |Natural exponential
f(x) = aˣ	                       |f'(x) = aˣ ln(a)	                 |General exponential
f(x) = ln(x)	                    |f'(x) = 1/x	                       |Natural logarithm
f(x) = log_a(x)	                 |f'(x) = 1/(x ln(a))                |General logarithm
## Trigonometric Functions		
f(x) = sin(x)	                    |f'(x) = cos(x) 	                 |Sine
f(x) = cos(x)	                    |f'(x) = -sin(x)	                 |Cosine
f(x) = tan(x)	                    |f'(x) = sec²(x) = 1/cos²(x)	     |Tangent
f(x) = cot(x)	                    |f'(x) = -csc²(x) = -1/sin²(x)	     |Cotangent
f(x) = sec(x)	                    |f'(x) = sec(x)tan(x)	              |Secant
f(x) = csc(x)	                    |f'(x) = -csc(x)cot(x)	           |Cosecant
## Neural Network Functions		                
f(x) = sigmoid(x) = 1/(1+e^(-x))	  |f'(x) = f(x)(1-f(x))	              |Sigmoid
f(x) = tanh(x)	                    |f'(x) = 1 - tanh²(x)	              |Hyperbolic tangent
f(x) = ReLU(x) = max(0,x)	        |f'(x) = {1 if x>0, 0 if x≤0}	     |Rectified Linear Unit
f(x) = Leaky ReLU(x)	              |f'(x) = {1 if x>0, α if x≤0}	     |Leaky ReLU (α≈0.01)
f(x) = softmax(x)	                 |Complex (see softmax section)	     |Softmax

## Derivatives of Neural Network Functions
🧠 First, understand a basic concept. In a Neural Network:
Input comes in.
A function is applied (Sigmoid / ReLU / Tanh)
An output is obtained
👉 The derivative indicates: whether the learning will be fast or slow.

### 🔥 1 . Sigmoid
👉 A function that converts the input to a value between 0 and 1.
👉 It is primarily used for probabilities.
📊 Formula  σ(x)=1 / (1 + e⁻ˣ)
➡️ derivative = f(x)(1 - f(x))

#### 🧠 Example 1.
👉 x = 0
σ(0)=1/1+e^0=1/2=0.5

#### 🧠 Example 2.
Find sigmoid derivative at x = 1
f(1) = 1 / (1 + e^(-1)) = 1 / (1 + 1/e) = 1 / (1 + 0.368) = 1 / 1.368 ≈ 0.731
f'(1) = f(1) · (1 - f(1)) = 0.731 · (1 - 0.731) = 0.731 · 0.269 ≈ 0.197

👉 x = 2 → ≈ 0.88
👉 x = -2 → ≈ 0.12

💡 Meaning
👉 Output 0.5 → learning fast
👉 Output 0 ya 1 → learning slow


#### 🧠 Example 3.
```python
sigmoid = 1 / (1 + e⁻ˣ)
print("sigmoid(x) =", sigmoid)
print("sigmoid'(x) =", diff(sigmoid, x))
print()
```

### 🔥2. ReLU   
👉 Converts negative values ​​to 0.
👉 Leaves positive values ​​unchanged.
Formula:    f(x)=max(0,x)
👉 x > 0 → 1
👉 x ≤ 0 → 0

#### 🧠 Example 1. Find ReLU derivative at x = 2
Since x = 2 > 0, f'(2) = 1

```python
print("ReLU derivative:")
print("x > 0  → 1")
print("x <= 0 → 0")
print()
```

### 🔥 3. TANH FUNCTION
👉 Outputs values ​​between -1 and +1
👉 A balanced version of the Sigmoid function
📊 Formula:    f(x) = tanh(x) = (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)
👉 derivative = 1 - tanh²(x)

Find tanh derivative at x = 1
tanh(1) = (e^1 - e^(-1)) / (e^1 + e^(-1)) = (e - 1/e) / (e + 1/e)
tanh(1) ≈ (2.718 - 0.368) / (2.718 + 0.368) = 2.350 / 3.086 ≈ 0.762
tanh'(1) = 1 - tanh²(1) = 1 - (0.762)² = 1 - 0.581 ≈ 0.419

```python
tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
print("tanh(x) =", tanh)
print("tanh'(x) =", diff(tanh, x))
print()
```

## 🤖 ML Connection
f(x) = Loss function
👉 The derivative indicates:➡️ Whether the loss is increasing or decreasing.


## 💥 One Line Summary
👉 Derivative = direction + speed of learning

👉 Derivative → Partial Derivative → Gradient → Gradient Descent

