reference = "CGCCCATATCACTCGAGACGTAAACTACGGCTGAATTATCCGCTACCTTCATGCCAATGGTGCCTCCATATTCTTTATCTGC"
seq3 = "CGCCCATACCACTCGAGACGTAAACTACGGCTGAAATATCCGCTACCTTCATGCCAATGGTGCGTCCATATTCTTTATCTGC"    
len_reference = len(reference)    
len_seq3 = len(seq3)    
print("Length of reference:" + str(len_reference))    
print()    
print("Length of seq3: " + str(len_seq3))
print()
len1 = len(reference)
len2 = len(seq3)
mismatches = 0
if len1 == len2: 
      for pos in range (0,len1) :
            if reference[pos] != seq3[pos]:
                  mismatches = mismatches + 1
                  print(pos,":",reference[pos],":",seq3[pos])
print("mismatches = ",mismatches)

