P = 10000  # Principal amount
R = 5      # Rate of interest per annum
T = 3      # Time in years

# Calculate Simple Interest
SI = (P * R * T) / 100

print(f"Simple Interest: ₹{SI}")


CI = P * ((1 + R / 100) ** T - 1)

print(f"Simple Interest: ₹{SI}")
print(f"Compound Interest: ₹{round(CI, 2)}")