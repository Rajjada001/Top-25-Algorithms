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
def partition(a,left,right):
    x = a[right]
    i = left
    for j in range(left,right):
        
        if a[j]<=x:
            a[i],a[j] = a[j],a[i]
            print("elements swapped:",a[i],a[j])
            i+=1
    a[i],a[right] = a[right],a[i]
    print("i=",i)
    print(a)

    return i

def quickSelect(a,l,r,k):

    if(k>0 and k<=r-l+1):
        index = partition(a,l,r)
    
        if(index-l ==k-1):
            return a[index]
        
        if(index-l > k-1):
            return quickSelect(a,l,index-1,k)
        
        return quickSelect(a,index+1, r, k-index+l-1)


# Driver Code
arr = [ 1,3,2,5,4 ]
n = len(arr)
k = 3
print(quickSelect(arr, 0, n - 1, k))
