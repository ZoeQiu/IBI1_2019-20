import matplotlib.pyplot 
#dna="ATGCTTCAGAAAGGTCTTACG"
dna=input("Write sequence here:")
dna_n={'A':0,'T':0,'C':0,'G':0}

#Add to dictionary
for A in dna:
    dna_n[A]=dna_n[A]+1
for G in dna:
    dna_n[A]=dna_n[A]+1
for C in dna:
    dna_n[A]=dna_n[A]+1
for T in dna:
    dna_n[A]=dna_n[A]+1
#Make the frequency dictionary
gene_dict={'A':dna_n[A],'G':dna_n[G],'C':dna_n[C],'T':dna_n[T]}
#Set labels and sizes 
labels = 'A','G','C','T'
sizes = (A,G,C,T)
colors = 'bule','red','green','pink'
explode = (0,0,0,0)
#Make the plot
plt.pie(sizes, explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False, startangle=50)
plt.axis('equal')
plt.show()

