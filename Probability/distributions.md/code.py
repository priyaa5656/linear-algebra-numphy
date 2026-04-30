# ==============================
# DISTRIBUTIONS PROJECT (FINAL)
# ==============================

import random
import matplotlib.pyplot as plt

print("🔥 DISTRIBUTION LEARNING PROJECT 🔥\n")

# ======================================
# 1. UNIFORM DISTRIBUTION (DICE)
# ======================================

print("=== UNIFORM DISTRIBUTION (DICE) ===")

results = []

# generate data (dice simulation)
for i in range(1000):
    num = random.randint(1, 6)
    results.append(num)

print("First 10 dice rolls:", results[:10])


# ======================================
# 2. COUNT FREQUENCY (SORTED)
# ======================================

count = {}

for num in results:
    count[num] = count.get(num, 0) + 1

print("\nFrequency count (sorted):")
for key in sorted(count):
    print(f"{key} : {count[key]}")


# ======================================
# 3. PLOT UNIFORM GRAPH
# ======================================

plt.hist(results, bins=[1,2,3,4,5,6,7], edgecolor='black')
plt.title("Uniform Distribution (Dice Simulation - 1000 Rolls)")
plt.xlabel("Dice Number")
plt.ylabel("Frequency")
plt.show()


# ======================================
# 4. NORMAL DISTRIBUTION
# ======================================

print("\n=== NORMAL DISTRIBUTION ===")

data = []

for i in range(1000):
    num = random.gauss(0, 1)  # mean=0, std=1
    data.append(num)

print("First 10 normal values:", data[:10])


# ======================================
# 5. MEAN CALCULATION (IMPORTANT)
# ======================================

mean = sum(data) / len(data)
print("Mean of data:", mean)


# ======================================
# 6. PLOT NORMAL GRAPH
# ======================================

plt.hist(data, bins=30, edgecolor='black')
plt.title("Normal Distribution (Mean=0, Std=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# ======================================
# END
# ======================================

print("\n✅ Project Completed Successfully!")