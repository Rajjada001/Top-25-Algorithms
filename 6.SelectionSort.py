def selectionSort(a):
    for i in range(len(a)):
        min_index = i

        for j in range(i+1,len(a)):
            if(a[j]<a[min_index]):
                min_index = j
            
        a[min_index],a[i] = a[i],a[min_index]
    
    return a

t = int(input("Enter no. of test cases: "))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    print(selectionSort(a))