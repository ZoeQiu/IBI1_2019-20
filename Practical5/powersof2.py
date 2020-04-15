#first, get a number
x=int(input("a number that is no larger than 8192:"))
o=str(x)+"is"
#because x<8192, n begins with 13
n=13
while (n>=0):
    if (2**n<=x):
        x=x-2**n
#the  output sentence 
        o=o+"2**+str(n)+"+"
        n=n-1
print(str(o))
        