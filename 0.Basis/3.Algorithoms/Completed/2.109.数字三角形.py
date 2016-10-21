class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    给定一个数字三角形，找到从顶部到底部的最小路径和。
    每一步可以移动到下面一行的相邻数字上。
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle)==None:
            return None
        if len(triangle)==1:
            return triangle[0][0]
        x=0
        y=0
        return self.getNodeMinimum(triangle,x,y)
        
    def getNodeMinimum(self,triangle,x,y):
        #每一步都是有与之对应下一步最优解
        if x<len(triangle)-1:
            minValue=min(self.getNodeMinimum(triangle,x+1,y),self.getNodeMinimum(triangle,x+1,y+1));
            print("orient:",minValue)
            print("step:",triangle[x][y])
            print("total:",triangle[x][y]+minValue)
            print()
            return triangle[x][y]+minValue
        else:
            print("total:",triangle[x][y])
            print()
            return triangle[x][y]
            
        
        
s=Solution()
value=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
result= s.minimumTotal(value)
print(type(result))
print(result)
