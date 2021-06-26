# There is a corridor in a Jail which is N units long. Given an array A of size N. The ith index of this array is 0 if the light at ith position is faulty otherwise it is 1.
# All the lights are of specific power B which if is placed at position X, it can light the corridor from [ X-B+1, X+B-1].
# Initially all lights are off.
# Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.

# Example Input
# Input 1:
# A = [ 0, 0, 1, 1, 1, 0, 0, 1].
# B = 3

# Input 2:
# A = [ 0, 0, 0, 1, 0].
# B = 3

# Example Output
# Output 1:
# 2

# Output 2:
# -1

# In this we are using greedy approach that we get to the rightmost position and if there is a working switch then we on it and move to the next B-1 position 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i=0
        res=0
        while i<len(A):
            j = i+B-1
            if j>len(A)-1:
                j=len(A)-1
            while j>0 and j>i-B+1:
                if A[j]==1:
                    res+=1
                    i=j+B
                    break
                else:
                    j-=1
            if((i-B+1)==j):
                return -1
                
        return res