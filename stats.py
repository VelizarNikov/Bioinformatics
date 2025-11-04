import collections

def base_count(genome):
     return collections.Counter(genome)

dna = "AGCTCATGCT" #example seq

def reverse_complement(seq):
     complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
     complement_dna = ""
     for base in seq[::-1]:
          complement_dna += complement_dict[base]
     return complement_dna
