'''
The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this). 
And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). 
Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far 

Algorithm:

Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

'''


def KadaneAlgo(a):
    max_sum = curr_sum = a[0]
    for i in range(1,len(a)):
        curr_sum += a[i]
        curr_sum = max(curr_sum, a[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum

t = int(input("Enter no of test cases:"))
for _ in range(t):
    a = list(map(int, input().rstrip().split()))
    print("Maximum contiguous sum is", KadaneAlgo(a))