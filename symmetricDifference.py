# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l1=list(map(int,input().strip().split()))
m=int(input())
l2=list(map(int,input().strip().split()))
l=list(set(l1)^set(l2))
for i in sorted(l):
    print(i)
