from string import *
s=input()
c=1
k=ascii_uppercase
l=[]
for i in s:
    if i in k:
        l.append(i)
print(len(l)+1)
