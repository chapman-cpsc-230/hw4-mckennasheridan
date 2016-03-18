
"""
File: count_pairs.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Counts the number of repeating base pairs in a DNA sequence.
"""

def count_pair(dna,base):
    i = 0
    for AT in dna:
        if AT == base:
            i+=1
        return dna.count(base)

dna = 'CAGGCACTTGATAT'
base = "AT"
n = count_pair(dna,base)
print('%s appears %d times in %s' % (base,n,dna))
