'''
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. 
Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. 
    Move the greater elements one position up to make space for the swapped element.
'''

def insertionSort(a,n):
    for i in range(1,n):
        key = a[i] #unsorted array

        j = i-1
        # Step two: compare it with the previous elements
        # This loop shifts all the elements to the right and
        # create a position for unsorted array
        while(j>=0 and key<a[j]):
            a[j+1] = a[j] 
            j-=1
        # This inserts the unsorted array in its correct position.
        a[j+1] = key

    return a

t = int(input('Enter test cases:'))
for _ in range(t):
    n = int(input())
    a = list(map(int, input().rstrip().split() ))
    print(insertionSort(a,n))