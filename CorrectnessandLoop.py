

def insertion_sort(n,arr):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            ind=i+1
            for j in range(ind):
                if arr[ind]<arr[j]:
                    arr[j],arr[ind]=arr[ind],arr[j]
    print(*arr)

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(m,ar)
#print(" ".join(map(str,ar)))
