#This code can be utilized to convert and RNA sequence into
#its respective translated protein sequence.
def rtop(seq):
    codon_map = {
      'AUG': 'M', 'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
      'ACG': 'T', 'ACA': 'T', 'ACU': 'T', 'ACC': 'T',
      'AAC': 'N', 'AAU': 'N',
      'AAG': 'K', 'AAA': 'K',
      'AGG': 'R', 'AGA': 'R',
      'AGC': 'S', 'AGU': 'S',
      'GUG': 'V', 'GUA': 'V', 'GUC': 'V', 'GUU': 'V',
      'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCU': 'A',
      'GAU': 'D', 'GAC': 'D',
      'GAG': 'E', 'GAA': 'E',
      'GGU': 'G', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G',
      'UUU': 'F', 'UUC': 'F',
      'UUA': 'L', 'UUG': 'L',
      'UCU': 'S', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S',
      'UAU': 'Y', 'UAC': 'Y',
      'UGU': 'C', 'UGC': 'C',
      'UGG': 'W',
      'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
      'CCU': 'P', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P',
      'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
      'CAU': 'H', 'CAC': 'H',
      'CAG': 'Q', 'CAA': 'Q'
  }
    protein_seq = ""
    start_index = seq.find("AUG")
    if start_index != -1:
        for i in range(start_index, len(seq), 3):
            codon = seq[i:i+3]
            if codon in ['UAG', 'UAA', 'UGA']:
                break
            protein_seq += codon_map.get(codon, '')
    return protein_seq 
