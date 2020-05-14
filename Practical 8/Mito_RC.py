#import model and open file
import re
import os
os.chdir("C:\\Users\\hh\\Desktop")
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
new_file=open('mito_gene.fa',"w")

#find all the mito genes by function 'findall'
f=a.read()
seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',f)
#creat a new file
newfile=open('mito_gene.fa',"w")
