#import the matplotlib
import matplotlib.pyplot as plt
#define a gene lenghth list
gene_lengths=input('the lengths:')
#sort the lenghth
gene_lengths.sort()
#print the original list
print("the original gene list: ",gene_lengths)
#delete the largest one
gene_lengths.pop()
#delete the smallest one
del(gene_lengths[0])
#print the new list without the largest and smallest one
print("the new sorted gene list without the largest and the smallest one: ",gene_lengths)
#specific details about the plot
plt.boxplot(gene_length,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=Ture
            ）
plt.show()

   