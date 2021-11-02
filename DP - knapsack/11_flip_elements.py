'''
Problem Statement: Given an array of positive elements, you have to flip the 
sign of some of its elements such that the resultant sum of the elements of 
array should be minimum non-negative (as close to zero as possible). 
Return the minimum no. of elements whose sign needs to be flipped such that
the resultant sum is minimum non-negative.
'''



def solve(arr):
    n = len(arr)
    s = sum(arr)
    
    dp = [[-1 for _ in range(2*s+1)] for _ in range(n+1)]
    
    def rec(i, w):
        if i == 0:
            if w == 0:
                return 0
            return 10**9
            
        if w > s or w < -s:
            return 10**9
            
        if dp[i][w+s] != -1:
            return dp[i][w+s]
        
        not_flipped = rec(i-1, w-arr[i-1])
        flipped = rec(i-1, w+arr[i-1])
        
        dp[i][w+s] = min(flipped + 1, not_flipped)
        return dp[i][w+s]
        
    
    for z in range(-s, s+1):
        rec(n, z)
        
    for k in range(s, 2*s+1):
        if dp[n][k] != 10**9:
            return dp[n][k]
        

print(solve([10, 22, 9, 33, 21, 50, 41, 60]))