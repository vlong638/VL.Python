class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    """
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。
    """
    def plusOne(self, digits):
        # Write your code here
        if len(digits)==0:
            return [1]
        self.plusOneByIndex(digits,len(digits)-1)
        return digits
        
    def plusOneByIndex(self,digits,index):
        if index==0:
            value=digits[index]+1
            if value>9:
                digits[index]=0
                digits.insert(0,1)
            else:
                digits[index]=value
        else:
            value=digits[index]+1
            if value>9:
                digits[index]=0
                self.plusOneByIndex(digits,index-1)
            else:
                digits[index]=value
            

        
s=Solution()
result= s.plusOne([1,1])
print(type(result))
print(result)
