seq = 'ATGCGACTACGATCGAGGGCCAT'
#creat a dictionary for the comlementary sequence
dictionary={'C':'G','A':'T','G':'C','T':'A'}
com_seq=''
for i in seq:
    com_seq+=dictionary[i]
#reverse the com_seq
reverse_com_seq=com_seq[::-1]
print(reverse_com_seq)
