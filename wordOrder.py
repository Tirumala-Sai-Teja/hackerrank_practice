# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for __ in range(n):
    s=input()
    if d.get(s,0)==0:
        d[s]=1
    else:
        d[s]=d.get(s)+1
print(len(d))
for i in d.keys():
    print(d.get(i),end=' ')
    
        
