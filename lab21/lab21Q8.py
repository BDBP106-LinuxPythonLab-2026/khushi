# (8) Write a function protein_energy_temp() with an inner function
# calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
# random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0).
T=float(input("enter a temperature: "))
H=float(input("enter the entalpy "))
S=float(input("enter the entropy"))

def protein_energy_temp():
    def calculate_free_energy(enthalpy,entropy):
        G= enthalpy - T *entropy
        print(G)
        if G < 0:
              print("stable")
        else:
              print("unstable")
    return calculate_free_energy(H,S)

print(protein_energy_temp())