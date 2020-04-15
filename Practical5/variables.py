
a=123
b=123124
b%7
c=b/7
d=c/11
e=d/13
print(e)
print(a)
#simple math
a=123
b=123123
#check if it could be divided by 7
if (b%7==0):
    print(" it can be devided by 7")
else:
    print(" it can not be devided by 7")
c=b/7
d=c/1
e=d/13
if (e<a):
    print("e><a")
elif (e=a):
    print("e=a")
else:
    print("e<a")
    #booleans
X=True
Y=True
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
if (Z==W):
    print("Z=W")
else:
    print("Z!=W")