'''
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. 
If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. 
Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

'''
def binarySearch(a,k,l,r):
    
    if l > r:
        return -1
    else:
        mid = l+(r-l)//2
        if(a[mid]>k):
            return binarySearch(a,k,l,mid-1)
        elif(a[mid]<k):
            return binarySearch(a,k,mid+1,r)
        else:
            return mid+1


t = int(input("Enter no. of test cases: "))
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    print("Element is at ",binarySearch(a,k,0,n)," position")
