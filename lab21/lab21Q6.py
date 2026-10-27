# (6) Write a function called cell_metabolism that takes the number of glucose and oxy-
# gen molcules, that contains an inner function energy_output() to calculate ATP yield
# (assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
# produced.
def cell_metabolism(glucose, oxygen):
    def energy_output():
        return min(glucose, oxygen // 6) * 38

    return energy_output()

g = int(input("Enter the number of glucose molecules: "))
o = int(input("Enter the number of oxygen molecules: "))

print("Total ATP produced:", cell_metabolism(g, o))