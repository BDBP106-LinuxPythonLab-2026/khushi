# (7) Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence.

a=["a","t","g","t","g","a","c","g","a","t","c","a","g"]
b=[i.upper() for i in a]
print(b)
def analyze_dna(b):
    def gc_content():
     x=b.count("G") + b.count("C")
     y=x/len(b)*100
     print(y)
     if y>50:
      print("gc rich")
     elif y<50:
      print("at rich")
    gc_content()
analyze_dna(b)