def count_nucleotides(dna, nucleotide):
    num_nucleodites=0
    for char in dna:
        if char == nucleotide:
            num_nucleodites=num_nucleodites + 1      
    return num_nucleodites
sequence = "CCCTACTTCACTCCAGTACTATAGTAGTAGCTGGGGTTTTCTTACTTATTCGCTTCCACCCACCAATAGAAAATAATACAACAATTCAAAGTCTTACACTATGCCTAGGAGCTATTACTACCATATTCATAGCAATCTGCGCCCTAACACAAAATGACATTAAAAAAATTGTAGCCTTCTCTACCTCAA"
A = count_nucleotides(sequence,"A")
T = count_nucleotides(sequence,"T")
G = count_nucleotides(sequence,"G")
C = count_nucleotides(sequence,"C")
print("A=",A)
print("T=",T)
print("G=",G)
print("C=",C)
x = ["A","T","G","C"]
y = [A,T,G,C]
import plotly
import plotly.express as px
fig = px.bar(x=["A", "T", "G","X"], y=[A, T, G, C])

fig.write_image("Ques01.png")
fig.show()
