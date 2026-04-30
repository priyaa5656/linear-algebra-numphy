# ==============================
# PROBABILITY BASICS PROJECT
# ==============================

# --------- 1. BASIC PROBABILITY ---------
print("=== BASIC PROBABILITY ===")

favorable = 1
total = 6

probability = favorable / total

print("Probability (1 out of 6):", probability)
print()


# --------- 2. CONDITIONAL PROBABILITY ---------
print("=== CONDITIONAL PROBABILITY ===")

# Example: Given even numbers, probability of 6

even_numbers = [2, 4, 6]
favorable = [6]

conditional_prob = len(favorable) / len(even_numbers)

print("P(6 | even):", conditional_prob)
print()


# --------- 3. BAYES THEOREM ---------
print("=== BAYES THEOREM ===")

# Example: Disease test

P_D = 0.01          # Probability of disease
P_P_given_D = 0.99  # Positive given disease
P_P = 0.05          # Total positive

P_D_given_P = (P_P_given_D * P_D) / P_P

print("P(Disease | Positive):", P_D_given_P)
print()


# --------- 4. USER INPUT (INTERACTIVE) ---------
print("=== TRY YOUR OWN VALUES ===")

P_A = float(input("Enter P(A): "))
P_B_given_A = float(input("Enter P(B|A): "))
P_B = float(input("Enter P(B): "))

result = (P_B_given_A * P_A) / P_B

print("P(A|B) =", result)
