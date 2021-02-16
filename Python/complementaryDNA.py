# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# You have function with one side of the DNA (string, except for Haskell); 
#you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# My original solution:

def DNA_strand(dna):
    arr = list(dna)
    new_arr = []
    for char in arr:
        if char == 'A':
            new_arr.append('T')
        elif char == 'T':
            new_arr.append('A')
        elif char == 'C':
            new_arr.append('G')
        elif char == 'G':
            new_arr.append('C')
            
    return ''.join(new_arr)



# Better Solution

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
