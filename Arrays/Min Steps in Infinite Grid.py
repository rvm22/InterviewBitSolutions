# You are in an infinite 2D grid where you can move in any of the 8 directions

#  (x,y) to 
#     (x-1, y-1), 
#     (x-1, y)  , 
#     (x-1, y+1), 
#     (x  , y-1),
#     (x  , y+1), 
#     (x+1, y-1), 
#     (x+1, y)  , 
#     (x+1, y+1) 

# You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.
# Example Input
# Input 1:
#  A = [0, 1, 1]
#  B = [0, 1, 2]

# Example Output
# Output 1:
#  2
#Here we are taking max(|x1-x2|,|y1-y2|) as the distance travelled to get from point(x1,y1) to (y1,y2)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        x = A[0]
        y = B[0]
        res = 0
        for i in range(len(A)):
            res+=max(self.modulus(x,A[i]),self.modulus(y,B[i]))
            x = A[i]
            y = B[i]
        return res
    def modulus(self,a,b):
        res = a-b
        if res>0:
            return res
        else:
            return res*-1

