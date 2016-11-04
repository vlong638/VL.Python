"""
给出一个有n个整数的数组S，
在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

 注意事项

在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。
"""
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        result=[]
        x=0
        numbers.sort()
        numbers=self.leave3(numbers)
        while x<len(numbers):
            y=len(numbers)-1
            while y>1:
                z=x+1
                while z<y:
                    if numbers[x]+numbers[y]+numbers[z]==0:
                        t=(numbers[x],numbers[z],numbers[y])
                        if t not in result:
                            result.append(t)
                    z+=1
                y-=1
            x+=1
        return result

    def leave3(self,numbers):
        result=[numbers[0]]
        count=1
        i=1
        while i<len(numbers):
            if numbers[i]==numbers[i-1]:
                count+=1
                if count<=3:
                    result.append(numbers[i])
            else:
                count=1
                result.append(numbers[i])
            i+=1
        return result



        
s=Solution()
print(s.threeSum([2,7,11,15]))
print(s.threeSum([-1,1,0]))
print(s.threeSum([1,0,-1,-1,-1,-1,0,1,1,1]))
print(s.threeSum([-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]))
