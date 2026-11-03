 # (9) A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
# sequence called a codon. For example, the sequence fragment AGTCTTATATCT con-
# tains the codons AGT, CTT, ATA, TCT if read from the first position. If read from
#
# the second position, it yields the codons GTC, TTA, TAT and if read from the third
# position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
#
# 3-letter strings given a sequence and from what position (input as an integer) the se-
# quence should be read. As an example, output the 3-letter strings from the sequence
#
# GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position.

def extract_codons(sequence, position):
    codons = []

    start = position - 1

    for i in range(start, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        codons.append(codon)

    return codons


dna = "GTTTCGATTATAACG"

# Read from 1st position
print("1st position:", extract_codons(dna, 1))

# Read from 3rd position
print("3rd position:", extract_codons(dna, 3))