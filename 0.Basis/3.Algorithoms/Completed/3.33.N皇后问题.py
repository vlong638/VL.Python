from copy import deepcopy  
class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    #将皇后的移动规则当作八方位移,以当前检测攻击方案
    def solveNQueens(self, n):
        print(n)
        self.n=n
        self.results=[]
        self.addNQueens([],0)
        return self.results

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
    
    #将皇后的移动规则当作八方位移,但是空间复杂度较高,复制了可选方案
    #可以简化空间复杂度,将其改为使用当前方案去检测是否可攻击
    def solveNQueens3(self, n):
        choices=[[0
                  for x in range(n)]                  
                  for y in range(n)]
        self.result=[]
        self.addNQueens3(n,choices,[],1)
        return self.result

    def addNQueens3(self,n,choices,curSolution,level):
        if len(curSolution)==n:
            self.result.append(curSolution)
            return
        index=0
        for choice in choices[level-1]:
            index+=1
            if choice==-1:
                continue
            tempChoices=deepcopy(choices)
            for templevel in range(level+1,n+1):
                tempChoices[templevel-1][index-1]=-1
                if index-1+templevel-level<n:
                    tempChoices[templevel-1][index-1+templevel-level]=-1
                if index-1-templevel+level>=0:
                    tempChoices[templevel-1][index-1-templevel+level]=-1
            line="."*(index-1)+"Q"+"."*(n-index)
            tempSolution=curSolution[:]
            tempSolution.append(line)
            self.addNQueens3(n,tempChoices,tempSolution,level+1)
        

    #将皇后的移动规则当作八方位移一格
    def solveNQueens2(self, n):
        # write your code here
        choices=list(range(0,n))
        self.result=[]
        self.addNQueens2(n,choices,[],-2)
        return self.result

    def addNQueens2(self,n,choices,curSolution,preIndex):
        if len(curSolution)==n:
            self.result.append(curSolution)
            return
        index=0
        for choice in choices:
            index+=1
            if choice==-1 or (index>preIndex-2 and index<preIndex+2):
                continue
            tempChoices=deepcopy(choices)
            line="."*(index-1)+"Q"+"."*(n-index)
            #print("line",line)
            tempChoices[index-1]=-1
            #print("tempChoices",tempChoices)
            #tempChoices.remove(choice)
            tempSolution=curSolution[:]
            tempSolution.append(line)
            self.addNQueens2(n,tempChoices,tempSolution,index)
        
  
s=Solution()
result= s.solveNQueens(1)
for line in result:
    print(line)
print()

result= s.solveNQueens(2)
for line in result:
    print(line)
print()

result= s.solveNQueens(3)
for line in result:
    print(line)
print()

result= s.solveNQueens(4)
for line in result:
    print(line)
print()

result= s.solveNQueens(5)
for line in result:
    print(line)
print()



