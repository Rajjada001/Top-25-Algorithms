'''
QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways. 

Always pick first element as pivot.  (implemented below)
Always pick last element as pivot
Pick a random element as pivot.
Pick median as pivot.

The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. 
All this should be done in linear time.

'''


def partition(a,l,r):

    # Pivot as the first element
    p_index = l
    pivot = a[p_index]

    while(l<r):
        while( l<len(a) and a[l]<=pivot):
            l+=1
        while(a[r]>pivot):
            r-=1
        
        if(l<r):
            a[l],a[r] = a[r],a[l]
    a[r],a[p_index] = a[p_index],a[r]

    return r



def QuickSort(a,l,r):
    
    if(l<r):

        p = partition(a,l,r)

        QuickSort(a,l,p)
        QuickSort(a,p+1,r)
    return a


# Test cases
t = int(input("Enter number of test cases:"))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    print(QuickSort(a,0,len(a)-1))
