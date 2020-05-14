
#import models
import re
import os
os.chdir("C:\\Users\\hh\\Desktop")
#input the data
user_file=input('Please input the name of your fasta file here:')
newfile=open(user_file,'w')
#open the Saccharomyces_cerevisiae file
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
seq_mito=re.findall(r'(>.*?:Mito:[\d\D]+?gene:.*\n[\d\D]+?)>',a.read())
#simplify
for gene in seq_mito:
    simplified_seq_mito=re.sub(r'>.*?(gene:.*? ).*?]',r'\1',gene)
    final=simplified_seq_mito.replace('\n','')
    length=len(final)-11
    b=">"+'gene length:'+str(length)+' '+final+"\n"
    reseq=''
#C&R
trantab=str.maketrans('ATGC','TACG')
string=b.translate(trantab)
reversed_string = string[::-1]
print('string:',reversed_string)
