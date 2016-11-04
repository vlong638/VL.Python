"""
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标,
并且第一个下标小于第二个下标。
注意这里下标的范围是 1 到 n，不是以 0 开头。

 注意事项

你可以假设只有一组答案。
"""
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        x=0
        while x<len(numbers):
            y=x+1
            while y<len(numbers):
                if numbers[x]+numbers[y]==target:
                    return [x+1,y+1]
                y+=1
            x+=1
        return None




        
s=Solution()
result= s.twoSum([2, 7, 11, 15],9)
print(result)
