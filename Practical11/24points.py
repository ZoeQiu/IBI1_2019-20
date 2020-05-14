#import necessary tools
import numpy as np
from itertools import permutations
 
 
#input the four unmders from users
a = int(input("the first interge here:"))
b = int(input("type the second interge from here:"))
c = int(input("type the third interge from here:"))
d = int(input("type the fourth interge from here:"))
points = [a, b, c, d]
symbols = ["+", "-", "*", "/"]
l1=[c for c in permutations(points,4)]

l2 =[]
# calculate the list for different permutation and combination
 
flag=False
 
for n in l1:
    one,two,three,four=n
    for s1 in symbols:
        for s2 in symbols:
            for s3 in symbols:
                if s1+s2+s3=="+++" or s1+s2+s3=="***":
#if just multiply or just add, the parentheses no longer make sense.
                    express = [ "{0} {1} {2} {3} {4} {5} {6}".format(one, s1, two, s2, three, s3, four)]  
                else:
                    express = [ "(({0} {1} {2}) {3} {4}) {5} {6}".format(one, s1, two, s2, three, s3, four),
                               "({0} {1} {2}) {3} ({4} {5} {6})".format(one, s1, two, s2, three, s3, four),
                               "(({0} {1} ({2} {3} {4})) {5} {6})".format(one, s1, two, s2, three, s3, four),
                               "{0} {1} (({2} {3} {4}) {5} {6})".format(one, s1, two, s2, three, s3, four),
                               "{0} {1} ({2} {3} ({4} {5} {6}))".format(one, s1, two, s2, three, s3, four)]
                
                for e in express:try:
                        if abs(eval(e)-24)<0.01:
                            l2.append(e+" = 24")
                            flag=True        
#Remove duplicates 
l3=set(list2)  
#print the result
for c in l3:
    print(c)
 
if flag==False:
    print("No")
