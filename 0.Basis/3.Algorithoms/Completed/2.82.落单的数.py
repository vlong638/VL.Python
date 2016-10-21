class Solution:
    """
    @param A : an integer array
    @return : a integer
    给出2*n + 1 个的数字，
    除其中一个数字之外其他每个数字均出现两次，
    找到这个数字。
    """
    def singleNumber(self, A):
        # write your code here
        if A==None or len(A)==0:
            return None
        dic={}
        for value in A:
            if dic.get(value):
                del dic[value]
            else:
                dic[value]=1
        for key in dic.keys():
            return key


s=Solution()
result=s.singleNumber([1,1,2,4,3,4,3])
print(result)
result=s.singleNumber([])
print(result)

