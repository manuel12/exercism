def to_rna(dna_strand):
  if dna_strand == "":
    return ""
  rna_strand = []
  for char in dna_strand:
    if char == "G":
      char = "C"
    elif char == "C":
      char = "G"
    elif char == "T":
      char = "A"
    elif char == "A":
      char = "U"
    rna_strand.append(char)
  return "".join(rna_strand)
