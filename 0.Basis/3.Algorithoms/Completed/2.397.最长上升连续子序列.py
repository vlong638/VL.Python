class Solution:
    def longestIncreasingContinuousSubsequence(self, A):
        if len(A)<=1:
            return 0
        maxLength=0
        length=1
        index=0
        while index<=len(A)-2:
            if  A[index]<A[index+1]:
                length+=1
                print("current",A[index],"next",A[index+1])
                print("length++,length",length)
            else:
                print()
                print("current",A[index],"next",A[index+1])
                print("reset,length",length)
                length=1
            if length>maxLength:
                maxLength=length
            index+=1
        length=1
        while index>=1:
            if  A[index]<A[index-1]:
                length+=1
                print("current",A[index],"next",A[index-1])
                print("length++,length",length)
            else:
                print()
                print("current",A[index],"next",A[index-1])
                print("reset,length",length)
                length=1
            if length>maxLength:
                maxLength=length
            index-=1
        return maxLength


s=Solution()
result= s.longestIncreasingContinuousSubsequence([5,4,2,1,3])
print(type(result))
print(result)


