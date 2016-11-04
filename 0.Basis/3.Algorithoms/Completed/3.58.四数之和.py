"""
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

 注意事项

四元组(a, b, c, d)中，需要满足a <= b <= c <= d

答案中不可以包含重复的四元组。
"""
class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self, numbers,target):
        result=[]
        x=0
        numbers.sort()
        if numbers[0]> target and numbers[len(numbers)-1]> target:
            return result
        if numbers[0]< target and numbers[len(numbers)-1]< target:
            return result
        numbers=self.leaveN(numbers,4)
        while x<len(numbers):
            y=len(numbers)-1
            while y>1:
                z=x+1
                while z<y:
                    w=z+1
                    while w<y:
                        if numbers[x]+numbers[z]+numbers[w]+numbers[y]==target:
                            t=(numbers[x],numbers[z],numbers[w],numbers[y])
                            if t not in result:
                                result.append(t)
                        w+=1
                    z+=1
                y-=1
            x+=1
        return result

    def leaveN(self,numbers,n):
        result=[numbers[0]]
        count=1
        i=1
        while i<len(numbers):
            if numbers[i]==numbers[i-1]:
                count+=1
                if count<=n:
                    result.append(numbers[i])
            else:
                count=1
                result.append(numbers[i])
            i+=1
        return result

s=Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2],0))
