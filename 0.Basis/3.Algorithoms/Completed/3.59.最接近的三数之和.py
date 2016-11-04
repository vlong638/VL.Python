"""
给一个包含 n 个整数的数组 S,
找到和与给定整数 target 最接近的三元组，返回这三个数的和。

 注意事项

只需要返回三元组之和，无需返回三元组本身
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        closest=numbers[0]+numbers[1]+numbers[2]
        x=0
        numbers.sort()
        numbers=self.leave3(numbers)
        while x<len(numbers):
            y=len(numbers)-1
            while y>1:
                z=x+1
                while z<y:
                    if abs(target-(numbers[x]+numbers[y]+numbers[z]))<abs(target-closest):
                        closest=numbers[x]+numbers[y]+numbers[z]
                        if closest==target:
                            return closest
                    z+=1
                y-=1
            x+=1
        return closest

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
print( s.threeSumClosest([-1, 2, 1, -4],1))
