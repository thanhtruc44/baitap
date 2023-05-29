input_strand = "CAACTGTCGTTTTCTCAACTAATAAAAATTTATTTCACACACCACCCTTGACACCTCCACCCACCTCTTCTTTCCCATAATCCCCAAAGATGGTATCATAATACCCATTATT"
reversed_strand = ""
length = len(input_strand)
for i in range(length):
    character = input_strand[length - 1 - i]
    if character == "A":
        reversed_strand = reversed_strand + "T"
    elif character == "T":
        reversed_strand = reversed_strand + "A"
    elif character == "G":
        reversed_strand = reversed_strand + "C"
    elif character == "C":
        reversed_strand = reversed_strand + "G"
    else:
        reversed_strand = reversed_strand + character
print("The input DNA strand is:", input_strand)
print("The reverse complement is:", reversed_strand)