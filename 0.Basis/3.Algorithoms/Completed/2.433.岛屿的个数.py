"""
给一个01矩阵，求不同的岛屿的个数。

0代表海，1代表岛，如果两个1相邻，
那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
"""
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if len(grid)<=0 or len(grid[0])<=0:
            return 0
        maxY=len(grid)-1
        maxX=len(grid[0])-1
        x,y=self.search(grid,maxX,maxY)
        count=0
        while x!=None:
            self.expungeByPoint(grid,x,y,maxX,maxY)
            count+=1
            self.display(grid)
            x,y=self.search(grid,maxX,maxY)
        return count
                
    def search(self,grid,maxX,maxY):
        x=0
        y=0
        while y<=maxY:
            while x<=maxX:
                if grid[y][x]==1:
                    print("return ",x,",",y)
                    return x,y
                else:
                    x+=1
            y+=1
            x=0
        print("return None")
        return None,None
    
    def expungeByPoint(self,grid,x,y,maxX,maxY):
        line=[]
        for n in range(0,x):
            line.append(0)
        while x<=maxX:
            if grid[y][x]==1:
                grid[y][x]=0
                line.append(1)
            else:
                x-=1
                break
            x+=1
        for n in range(x,maxX):
            line.append(0)
        
        self.expungeByLine(grid,line,y+1,maxX,maxY)
        
    def expungeByLine(self,grid,line,y,maxX,maxY):
        if y>maxY or y<0:
            return
        if 1 not in line:
            return
        x=0
        currentLine=[]
        for n in range(0,maxX+1):
            currentLine.append(0)
        while x<=maxX:
            if line[x]==1:
                if grid[y][x]==1:
                    grid[y][x]=0
                    currentLine[x]=1
                    c=x-1
                    while c>=0:
                        if grid[y][c]==1:
                            grid[y][c]=0
                            currentLine[c]=1
                        else:
                            break
                        c-=1
                    c=x+1
                    while c<=maxX:
                        if grid[y][c]==1:
                            grid[y][c]=0
                            currentLine[c]=1
                        else:
                            break
                        c+=1
            x+=1
            
        self.expungeByLine(grid,currentLine,y-1,maxX,maxY)
        self.expungeByLine(grid,currentLine,y+1,maxX,maxY)

    def display(self,grid):
        x=0
        while x<len(grid):
            print(grid[x])
            x+=1
        print()



        
s=Solution()
result= s.numIslands([
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
])
print(type(result))
print(result)
