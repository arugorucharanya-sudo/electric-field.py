# Electric Field Calculation

 Coulomb's constant
k = 9 * 10**9

Input values
Q = float(input("Enter charge (C): "))
r = float(input("Enter distance from charge (m): "))

 Calculate electric field
E = (k * abs(Q)) / (r ** 2)

 Display result
print("\n--- Electric Field Calculation ---")
print("Charge =", Q, "C")
print("Distance =", r, "m")
print("Electric Field =", E, "N/C")
