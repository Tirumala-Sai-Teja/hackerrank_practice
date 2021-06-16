from string import ascii_lowercase as al
def print_rangoli(size):
    n1=2*(2*size-1)-1
    a=al
    gap=n1//2
    s=size
    for i in range(size):
        print('-'*gap,end='')
        p=2*i+1
        for j in range(p//2):
            print(str(a[s-1]),end='-')
            s-=1
        for j in range(s-1,size-1):
            print(a[j],end='-')
        s=size
        print(str(a[s-1])+'-'*gap)
        gap-=2
    gap=2
    for i in range(size-2,-1,-1):
        
        print('-'*gap,end='')
        p=2*i+1
        for j in range(p//2):
            print(str(a[s-1]),end='-')
            s-=1
        for j in range(s-1,size-1):
            print(a[j],end='-')
        s=size
        print(str(a[s-1])+'-'*gap)
        gap+=2
 
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
