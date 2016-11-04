class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A = sorted(A, reverse=True)
        #A.sort()
        return A,A[k-1]
s=Solution()
a=[9,3,2,4,8]
b,result= s.kthLargestElement(2,a)
print(b)
print(result)
