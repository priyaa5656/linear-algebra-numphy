## 🧠 OPTIMIZATION (Machine Learning)
👉 Optimization = finding best parameters to minimize loss
👉 In ML, we create a function (a loss function). This tells us: how inaccurate the model is.
## 🎯 Goal
👉 The goal of Machine Learning is: “To minimize the loss or error” 📉

## 🏔️ Easy Real-Life Example Imagine this:
👉 You are standing on a hill in the dark. 
You need to get down (to the very bottom point).
But here's the problem: You don't have the full map. You can only feel the slope under your feet

🎯 What would you do?
👉 You would take a step in the direction where the ground slopes downward.
Then you would check again.Then take another step. 
by doing this repeatedly, you will eventually reach the bottom.
This is exactly what Optimization is.
👉 Going down step-by-step = Optimization, 
👉choose the Direction = Gradient


## 🧠 Local vs Global Minimum
👉 Imagine you're walking along a path and encounter a small dip.You stop right there ❌ (Incorrect).The lowest point was actually further ahead ✔ (Best)

👉 Local Minimum:
- Small dip
- Can trap the model ❌
👉 Smallest dip = Local Minimum

👉 Global Minimum:
- Lowest point
- Best solution ✔️
👉 The absolute lowest point = Global Minimum



   \      /
    \    /   ← local min
     \__/  

        \      /
         \    /
          \__/   ← global min 🎯



## 🧠 Convex vs Non-Convex
👉 Convex Function:
- One minimum ✔️
- Easy optimization
✔ Simple bowl shape → Easy (Convex)

👉 Non-Convex Function:
- Multiple minima ❗
- Can confuse the model
❌ Irregular, bumpy terrain → Confusing (Non-convex)

## 🧠  Learning Rate (α)
👉 Represents the step size (how big a step to take)
- Too large → overshoot ❌  
- Too small → slow 🐢  
- Perfect → smooth convergence ✔️


## 🧪 Example
f(x) = x²
Start: x = 2

Step 1:  Gradient = 2x = 4  
          New x = 1.6  

Step 2:  new Gradient = 2*1.6= 3.2  
New x = 1.28  
...
👉 Eventually x → 0 (minimum)

## 💥 One-Line Summary

👉 Optimization = process of minimizing loss using gradient descent

