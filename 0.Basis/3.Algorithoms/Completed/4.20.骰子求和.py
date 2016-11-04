class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here        
        result=[[0 for x in range(0,6*n)]
                for y in range(n)]
        for x in range(1,7):
            result[0][x-1]=1
        index=1
        while index<n:
            for y in range((index-1)+1,6*((index-1)+1)+1):#range((index-1)-1,(6**index+1-1)-1):
                pre=result[index-1][y-1]
                for x in range(1,7):
                    result[index][y+x-1]+=pre
            index+=1
        choices=6**n-n+1
        result2=[]
        for x in range(n,6*n+1):
            result2.append([x,round(result[n-1][x-1]/choices,3)])
        return result2

        




        
s=Solution()
result= s.dicesSum(1)
print(result)
print()

result= s.dicesSum(2)
print(result)
print()

result= s.dicesSum(3)
print(result)
print()

result= s.dicesSum(15)
print(result)
print()
