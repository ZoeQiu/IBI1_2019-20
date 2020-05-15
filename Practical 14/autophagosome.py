#import necessary model and data
import xml.dom.minidom as xdm
import pandas as pd

#define a function to find the number of childnotes
def num_cn(n_1):
    global terms
#count the childnotes
    cn=0
    
#get is_a
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        
        for parent in is_a:
            
            #if is_a parent
            if parent.childNodes[0].data==n_1:
                cn+=1
                
                #count children of the child
                cn_2=term.getElementsByTagName('id')[0].childNodes[0].data
                cn+=num_cn(cn_2)
return cn
#creat a list to store id
id=[]
#creat a list to store name
name=[]
#creat a list to store 'defstr'
definition=[]
#creat a list to store number of nodes
childnodes=[]
#open xml file

domtree=xdm.parse('go_obo.xml')
d=domtree.documentElement
#get all terms
terms=d.getElementsByTagName('term')
#get all contents in <defstr>
for term in terms:
    define=term.getElementsByTagName('def')[0]
    defstr=define.getElementsByTagName('defstr')[0].childNodes[0].data
    #autophagosome found
    if d.find('Autophagosome')>-1 or d.find('autophagosome')>-1:
   
    #add ID and name to the defstr
        n_1=term.getElementsByTagName('id')[0].childNodes[0].data
        id.append(n1)
        name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        definition.append(d)
        #add the number of childnodes to the list
        childnodes.append(num_cn(n_1))
#output the data into an excel file
data={'ID':id,'Name':name,'definition':definition,'childnodes':childnodes}
dataframe=pd.DataFrame(data)
dataframe.to_excel(r'C:\\Users\\hh\Desktop\\autophagosome.xlsx')
print('The file has been created successfully!')
