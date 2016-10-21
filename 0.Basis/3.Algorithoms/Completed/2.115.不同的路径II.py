class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        x=0
        y=0
        maxX=len(obstacleGrid)-1
        maxY=len(obstacleGrid[0])-1
        print("x",maxX)
        print("y",maxY)
        return self.getNextStep(obstacleGrid,x,y,maxX,maxY)

        
    def getNextStep(self,obstacleGrid,x,y,maxX,maxY):
        if obstacleGrid[x][y]==1:
            return 0
        elif x==maxX and y==maxY:
            return 1
        elif x==maxX:
            return self.getNextStep(obstacleGrid,x,y+1,maxX,maxY)
        elif y==maxY:
            return self.getNextStep(obstacleGrid,x+1,y,maxX,maxY)
        else:
            return self.getNextStep(obstacleGrid,x+1,y,maxX,maxY)+self.getNextStep(obstacleGrid,x,y+1,maxX,maxY)
        
s=Solution()
value=[
  [0,0,0,0],
  [0,1,0,0],
  [0,0,0,0]
]
result= s.uniquePathsWithObstacles(value)
print(result)
value2=[[0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
result= s.uniquePathsWithObstacles(value2)
print(result)
