#import sequence

human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
#set the initial distance as zero
d1=0
d2=0
d3=0

#set initial distance as 0
d1=0
d2=0
d3=0
#compare the two sequence and calculate the number of the animo acids that are same between two sequences
for i in range(len(human)):
    if random[i]!=human[i]:
        d1+=1
    if mouse[i]!=human[i]:
        d2+=1
    if random[i]!=mouse[i]:
        d3+=1
     
#print the result of the comparison
print('the genetic distance between human and random'+":"+str(d1))
print('the genetic distance between human and mouse'+":"+str(d2))
print('the genetic distance between mouse and random'+":"+str(d3))
#from the result, we can draw a conclusion that mouse is more familar with huaman than random sequence, genetically.
