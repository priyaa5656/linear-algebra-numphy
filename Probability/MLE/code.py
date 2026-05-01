# ==============================
# MLE + OUTLIER ANALYSIS PROJECT
# ==============================

import statistics

print("🔥 MLE (Maximum Likelihood Estimation) PROJECT 🔥\n")

# ======================================
# FUNCTION: ANALYZE DATA
# ======================================

def analyze_data(data):
    print("Data:", data)

    # Mean (MLE)
    mean = sum(data) / len(data)

    # Median
    median = statistics.median(data)

    print("Mean (MLE):", mean)
    print("Median:", median)

    # Insight
    if abs(mean - median) > 2:
        print("⚠️ Outlier detected → Mean may be misleading")
    else:
        print("✅ Data is balanced → Mean is reliable")

    print("-" * 40)


# ======================================
# CASE 1: NORMAL DATA
# ======================================

print("=== CASE 1: NORMAL DATA ===")
data1 = [2, 4, 6, 8]
analyze_data(data1)


# ======================================
# CASE 2: SLIGHT VARIATION
# ======================================

print("\n=== CASE 2: SLIGHT VARIATION ===")
data2 = [2, 2, 2, 3]
analyze_data(data2)


# ======================================
# CASE 3: OUTLIER PRESENT
# ======================================

print("\n=== CASE 3: OUTLIER DATA ===")
data3 = [2, 2, 2, 10]
analyze_data(data3)


# ======================================
# CASE 4: EXTREME OUTLIER
# ======================================

print("\n=== CASE 4: EXTREME OUTLIER ===")
data4 = [1, 2, 3, 100]
analyze_data(data4)


# ======================================
# USER INPUT (OPTIONAL)
# ======================================

print("\n=== TRY YOUR OWN DATA ===")

user_input = input("Enter numbers separated by space: ")

# convert input to list
user_data = list(map(int, user_input.split()))

analyze_data(user_data)


# ======================================
# END
# ======================================

print("\n✅ MLE Analysis Completed!")