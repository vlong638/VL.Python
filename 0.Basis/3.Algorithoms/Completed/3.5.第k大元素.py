class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A = sorted(A, reverse=True)
        #A.sort()
        return A[k-1]
s=Solution()
result= s.kthLargestElement(4,[9,3,2,4,8])
print(type(result))
print(result)
