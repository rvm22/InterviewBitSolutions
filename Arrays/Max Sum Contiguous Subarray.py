# Find the contiguous subarray within an array, A of length N which has the largest sum.
# Input 1:
#     A = [1, 2, 3, 4, -10]
# Output 1:
#     10
# Explanation 1:
#     The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
# Input 2:
#     A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output 2:
#     6
# Explanation 2:
#     The subarray [4,-1,2,1] has the maximum possible sum of 6.

#This problem is also called as Kadanes algorithm
#In this problem we find the maximum sum till the last position and if its sum with the next value is greater than the value at that position then we continue till the last position/ 

# @param A : tuple of integers
# @return an integer
def maxSubArray(self, A):
        temp = A[0]
        maxv = A[0]
        for i in range(1,len(A)):
            temp+=A[i]
            if temp<A[i]:
                temp = A[i]
            if temp > maxv:
                maxv = temp
        
        return maxv