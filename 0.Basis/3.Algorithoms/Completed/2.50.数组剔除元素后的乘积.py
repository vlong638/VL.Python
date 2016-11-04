class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        result=[]
        x=0
        while x<len(A):
            value=1
            y=0
            while y<len(A):
                if x!=y:
                    value*=A[y]
                y+=1
            result.append(value)
            x+=1
        return result



s=Solution()
result= s.productExcludeItself([1, 2, 3])
print(result)
