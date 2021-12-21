'''
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
The mergeSort() function is used for merging two halves.

```
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```
'''

def MergeSort(a):
    if(len(a)>1):
        mid = len(a)//2
        # left array
        left = a[:mid]
        # Right array
        right = a[mid:]

        # Merge Sort Left array
        MergeSort(left)
        # Merge Sort right array
        MergeSort(right)
        # initialize variables
        i=j=k=0
        while(i< len(left) and j<len(right)):
            # Compare the elements of left array to the right array
            if(left[i]<right[j]):
                a[k] = left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        # Add the remaining elements of left array
        while(i<len(left)):
            a[k]=left[i]
            i+=1
            k+=1
        # Add the remaining elements of right array
        while(j<len(right)):
            a[k]=right[j]
            j+=1
            k+=1
    return a


# Test cases
t = int(input("Enter number of test cases:"))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    print(MergeSort(a))