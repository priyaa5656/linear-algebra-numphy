# PROBABILITY BASICS
Probability = The chance of an event occurring.
If something has the potential to happen in the future, we refer to the "chance" of it happening as probability.

## 👉 The value is always:
0 = Impossible ❌  , 1 = Certain to happen ✅
Somewhere in between = It might happen / It might not

## 🌍 Real-Life Analogy
👉 Coin toss 🎲
Heads or Tails
Total outcomes = 2
👉 Probability (Heads) = 1/2
👉 Probability (Tails) = 1/2
This means a 50% chance 👍

## ❓ Why Does Probability Exist?
The real world is uncertain
Will it rain tomorrow? 🌧️
Will the stock market rise? 📈
Will the model make an accurate prediction? 🤖
👉 Probability is used to measure this uncertainty.

## FORMULA:
P(A) = (Favorable Outcomes) / (Total Outcomes)

### 🔍 Terms Explained
P(A) → The probability of event A
Favorable → The outcome we desire
Total → All possible cases

## SOLVED EXAMPLES
✅ Example 1: Coin
### Q: What is the probability of getting Heads?
👉 Favorable = 1 (Heads)
👉 Total = 2 (Heads, Tails)
👉 Answer = 1/2

✅ Example 2: Dice 🎲
### Q: What is the probability of rolling a 3?
👉 Total = 6 (1–6)
👉 Favorable = 1
👉 Answer = 1/6

✅ Example 3:
### Q: What is the probability of rolling an even number (2, 4, 6)?
👉 Favorable = 3
👉 Total = 6
👉 Answer = 3/6 = 1/2

✅ Example 4:
### Q: What is the probability of rolling an odd number?
👉 Favorable = 3 (1, 3, 5)
👉 Answer = 3/6 = 1/2

## PRACTICE QUESTIONS Give these a try 👇
What is the probability of rolling a 5 on a die?
What is the probability of getting Tails on a coin toss?
What is the probability of rolling a number > 4 on a die? 
Even number probability?
Number < 3?

✅ Answers:
1/6
1/2
2/6 = 1/3
3/6 = 1/2
2/6 = 1/3

```python
# Probability calculation
favorable = 1
total = 6
probability = favorable / total
print("Probability:", probability)
```

## AI RESEARCHER CONNECTION 🤖
👉 AI models make guesses: Example:
Is it a spam email or not?
Is there a cat or a dog in the image?
👉 The model says:
cat = 0.8
dog = 0.2
👉 This is probability!



# CONDITIONAL PROBABILITY
👉 Conditional = “dependent on a specific condition”
👉 Probability = chance
👉Conditional Probability = the probability of an event occurring when a certain condition is already true.

## 💡 difference 
👉 Normal: full sample space
👉 Conditional: reduced sample space

### 👉 Normal Probability:
“What is the probability of rolling a 6?”
### 👉 Conditional Probability: 
“If the number rolled is EVEN, what is the probability of it being a 6?”

---

## 🌍 Real-Life Analogy
 Imagine a bag 🎒 containing balls:
3 Red 🔴 and 2 Blue 🔵
👉 Total = 5

Normal Question: 👉 Probability of picking a Red ball = 3/5

Conditional Question: 👉 If ball is RED, what is probability of picking a specific red ball?
👉 Now, we are looking only within the set of RED balls.

## ❓ Why does this exist?
In the real world, we are constantly receiving new information:
“The student passed.”
“It is raining.”
“The user is male.”
👉 The probability changes once new information becomes available.👉 This is precisely what is known as Conditional Probability.

## FORMULA
P(A | B) = {P(A ∩ B)}/{P(B)}

### 🔍Terms Explained
P(A | B) → probability of A given B
P(A ∩ B) → both A and B together
P(B) → condition

## Solved Examples
✅ Example 1: Dice
### Q: If the number is EVEN, what is the probability of getting 6?
👉 Even numbers = {2,4,6} → total = 3
👉 Favorable = {6} → 1
👉 Answer = 1/3


✅ Example 2:
### Q: If number > 3, what is the probability of even number?
👉 >3 = {4,5,6} → total = 3
👉 Even = {4,6} → 2
👉 Answer = 2/3


✅ Example 3:
Cards example 🃏
👉 Total = 52
👉 Red = 26
👉 King = 4
👉 Red King = 2
### Q: If the card is RED, what is the probability of getting King?
Red card = 26 , Red King = 2
👉 Answer = 2/26 = 1/13

### Practice Questions Try it

Dice: given even, probability of 2?                 ✅ Answers = 1/3  
Dice: given >4, probability of 6?                   ✅ Answers = 1/2
Cards: given red, probability of Queen?             ✅ Answers = 2/26= 1/13  
Dice: given odd, probability of 5?                  ✅ Answers = 1/3
Dice: given <4, probability of even?                ✅ Answers = 1/3  

```python 
# Conditional probability example
even = [2, 4, 6]
favorable = [6]
probability = len(favorable) / len(even)
print("Conditional Probability:", probability)
```
🧠Explanation
made a list
len() = count
divide = probability


## AI CONNECTION🤖
👉 Spam detection:“If the email contains the word ‘FREE’, what is the probability of it being spam?” 👉 This is conditional probability!



## 🔑 Key Points
The sample space has changed due to condition.
Formula: P(A|B)
AI is used a lot

## :🚀 BAYES THEOREM
👉 Bayes = A mathematician (Thomas Bayes)
## 👉 Theorem: “Update your probability after receiving new information.”

## 🌍 Real-Life Analogy (VERY IMPORTANT)
👉 The Doctor & Test Example 🏥
The disease is rare (affects 1% of people).
The test result comes back positive. 😨
👉 Question: “Do I actually have the disease?”

👉 This is where Bayes comes into play.
👉 Naive Thinking: Test positive → Disease. ❌ This could be wrong.

👉 Correct Thinking:
How accurate is the test?
How rare is the disease?

👉 Bayes combines all of these factors.

## FORMULA
P(A | B) = (P(B | A) * P(A)) / P(B)

🔍Terms Explained
P(A|B) → final answer (after knowing B)
P(B|A) → if A is true then how likely is B
P(A) → initial belief
P(B) → overall probability

🧠 Easy language: 👉 Posterior = Likelihood × Prior / Evidence (keep in mind for future 🔥)

## SOLVEDEXAMPLE

✅ Example 1: Disease
### Q.
👉 P(Disease) = 0.01
👉 P(Positive | Disease) = 0.99
👉 P(Positive) = 0.05
👉 P(Disease | Positive)=? 

P(Disease | Positive)= (0.99 × 0.01) / 0.05 
P(Disease | Positive)= 0.0099 / 0.05 
P(Disease | Positive)= 0.198
✅ Answer: 👉 ~ 19.8%

💥 Shock intuition
👉 Even after being tested positive, the disease chance is only 19.8% 😳
👉Why? 👉 Disease is rare!


## PRACTICE QUESTIONS Try it 👇

P(A)=0.2, P(B|A)=0.5, P(B)=0.25                 ✅ Answers=0.4
P(A)=0.5, P(B|A)=0.8, P(B)=0.4                  ✅ Answers = 1.0
P(A)=0.1, P(B|A)=0.9, P(B)=0.3                  ✅ Answers=0.3
P(A)=0.3, P(B|A)=0.6, P(B)=0.5                  ✅ Answers=0.36
P(A)=0.4, P(B|A)=0.7, P(B)=0.2                  ✅ Answers=1.4⚠️ If answer > 1 → invalid inputs


```python 
# Bayes Theorem Example

# Step 1: Given values
P_D = 0.01          # Disease probability
P_P_given_D = 0.99  # Positive test given disease
P_P = 0.05          # Total positive probability

# Step 2: Apply Bayes formula
P_D_given_P = (P_P_given_D * P_D) / P_P

# Step 3: Print result
print("Probability of Disease given Positive:", P_D_given_P)
```


## AI CONNECTION 🤖
👉 Spam filter:
👉 P(Spam | “Free” word)
👉 Bayes uses: 
     word frequency 
     prior probability
👉 Gmail uses this technology 🔥


## 🔑 Key Points
extension of conditional probability
Prior → Posterior
super important in AI


## Summary
Conditional probability = updated probability after knowing something
Bayes = updating probability after new information
