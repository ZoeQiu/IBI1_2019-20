
#import model and open file
import re
import os
os.chdir("C:\\Users\\hh\\Desktop")
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
new_file=open('mito_gene.fa',"w")

#find all the mito genes by function 'findall'

seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',a.read)
#creat a new file
newfile=open('mito_gene.fa',"w")
l=[]
#simplify the unnecessary part
for gene in seq_mito:

    simplified_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
#replace the '\n' and '>'
    final=simplified_seq_mito.replace('\n','')
    length=len(final)-11
    e=">"+'gene length:'+str(length)+' '+final+"\n"
    l.append(e)
    newfile.write(e)
#close the newfile
newfile.close()
#print the final result
print(open('mito_gene.fa').read())
