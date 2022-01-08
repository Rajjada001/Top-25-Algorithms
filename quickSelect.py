'''
function quickSelect(list, left, right, k)

   if left = right
      return list[left]

   Select a pivotIndex between left and right

   pivotIndex := partition(list, left, right, 
                                  pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1 
'''


def quickSelect(a,l,r,k):
    # For the k largest element
    # k = len(a)-k  
    print(k)
    def partition(a,left,right):
        x = a[right]
        i = left
        for j in range(left,right):
            if a[j]<=x:
                a[i],a[j] = a[j],a[i]
                i+=1
        a[i],a[right] = a[right],a[i]

        return i

    p = partition(a,l,r)
    if p>k:
        return quickSelect(a,l,p-1,k)
    elif(p<k):
        return quickSelect(a,p+1,r, k)
    else:
        return a[p]


# Driver Code
arr = [ 1,3,2,5,4,0 ]
n = len(arr)
k = 2
print("ANS=",quickSelect(arr, 0, n - 1, k))
