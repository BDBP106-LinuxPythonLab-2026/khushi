# (8) Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence. (copy this code from Lab 21 to Lab 22 folder)

def analyse_dna(sequence):
    def gc_content():
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / len(sequence)) * 100

    gc_percentage = gc_content()

    print("GC Content:", round(gc_percentage, 2), "%")

    if gc_percentage > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")


analyse_dna("ATGCGCAT")