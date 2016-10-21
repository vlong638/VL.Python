class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    给定一个只含非负整数的m*n网格
    找到一条从左上角到右下角的可以使数字和最小的路径。
    """
    def minPathSum(self, grid):
        # write your code here
        if grid==None:
            return None
        x=0
        y=0
        maxX=len(grid)
        maxY=len(grid[0])
        return self.getMinNextStep(grid,x,y,maxX,maxY)
        

    def getMinNextStep(self,grid,x,y,maxX,maxY):
        if x==maxX-1 and y==maxY-1:
            self.display(0,grid[x][y],grid[x][y])
            return grid[x][y]
        elif x==maxX-1:
            orient=self.getMinNextStep(grid,x,y+1,maxX,maxY)
            self.display(orient,grid[x][y],orient+grid[x][y])
            return grid[x][y]+orient
        elif y==maxY-1:
            orient=self.getMinNextStep(grid,x+1,y,maxX,maxY)
            self.display(orient,grid[x][y],orient+grid[x][y])
            return grid[x][y]+orient
        else:
            orient=min(self.getMinNextStep(grid,x+1,y,maxX,maxY),self.getMinNextStep(grid,x,y+1,maxX,maxY))
            self.display(orient,grid[x][y],orient+grid[x][y])
            return grid[x][y]+orient

    def display(self,orient,step,total):
        print("orient:",orient)
        print("step:",step)
        print("total:",total)
        print()
    



        
s=Solution()
result= s.minPathSum([
    [0,3,8,5,5]
    ,[9,1,3,1,4]
    ,[0,3,8,5,5]
    ,[9,1,3,1,4]
    ,[9,1,3,1,4]
    ])
print(type(result))
print(result)
