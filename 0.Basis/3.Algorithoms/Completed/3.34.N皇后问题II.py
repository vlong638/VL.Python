"""
根据n皇后问题，现在返回n皇后不同的解决方案的数量而不是具体的放置布局。
"""
class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        print(n)
        self.n=n
        self.results=[]
        self.addNQueens([],0)
        return len(self.results)

    def addNQueens(self,preChoices,level):
        #n append preChoices as a Solution to Results
        if len(preChoices)==self.n:
            result=[]
            index=0
            for x in preChoices:
                line="."*x+"Q"+"."*(self.n-x-1)
                result.append(line)
                index+=1
            self.results.append(result)
            return

        for col in range(0,self.n):
            if self.attack(preChoices,col):
                continue
            tempPreChoices=preChoices[:]
            tempPreChoices.append(col)
            self.addNQueens(tempPreChoices,level+1)
            
    def attack(self,preChoices,col):
        if col in preChoices:
            return True
        row=len(preChoices)
        r=0
        while r<row:
            if preChoices[r]-(row-r)==col:
                return True
            if preChoices[r]+(row-r)==col:
                return True
            r+=1
        return False

s=Solution()
result= s.rotateString("abcd123456789",2)
print(type(result))
print(result)
