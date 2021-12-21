'''
The Euclidean algorithm, or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two integers (numbers),
 the largest number that divides them both without a remainder.
'''

def gcd(a,b):
    if a==0:
        return b
    else:
       return gcd(a%b,a)
    
t = int(input("Enter number of test cases"))

for _ in range(t):
    a,b= map(int, input().split())
    print(gcd(a,b))
