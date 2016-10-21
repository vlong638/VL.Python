import datetime
class Solution:
#有一个机器人的位于一个M×N个网格左上角（下图中标记为'Start'）。
#机器人每一时刻只能向下或者向右移动一步。
#机器人试图达到网格的右下角（下图中标记为'Finish'）。
#问有多少条不同的路径？

    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        x=0
        y=0
        maxX=m
        maxY=n
        return self.getNextStep(x,y,maxX,maxY)
        

    def getNextStep(self,x,y,maxX,maxY):
        if x==maxX-1 and y==maxY-1:
            return 1
        elif x==maxX-1:
            return 1
        elif y==maxY-1:
            return 1
        else:
            return self.getNextStep(x+1,y,maxX,maxY)+self.getNextStep(x,y+1,maxX,maxY)
        
        """优化效率
        elif x==maxX-2:
            return maxY-y
        elif y==maxY-2:
            return maxX-x
        """

s=Solution()
datetime1=datetime.datetime.now()    
result= s.uniquePaths(8,8)
"""
17,11
timespan: 0:00:01.231493
6619239

27,11
timespan: 0:00:51.651450
306638112
"""
datetime2=datetime.datetime.now()
print("timespan:",datetime2-datetime1)
print(result)
