class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    #给你一个包含 m x n 个元素的矩阵 (m 行, n 列), 求该矩阵的之字型遍历。
    #下意识结成与目标不符的方向了..略过
    #------>
    #<------
    #------>
    #<------
    """目标样例
对于如下矩阵：

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
返回 [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
"""
    
    
    def printZMatrix(self, matrix):
        x=0
        y=0
        result=[]
        maxY=len(matrix)-1
        if maxY<0:
            return []
        maxX=len(matrix[0])-1
        if maxX<0:
            return []
        side=True
        print("x",x,"y",y,"result.append",matrix[y][x])
        result.append(matrix[y][x])
        while y<=maxY:
            if side:
                while x<maxX:
                    x+=1
                    result.append(matrix[y][x])
                    print("x",x,"y",y,"result.append",matrix[y][x])
            else:
                while x>0:
                    x-=1
                    result.append(matrix[y][x])
                    print("x",x,"y",y,"result.append",matrix[y][x])
            y+=1
            if side:
                side=False
            else:
                side=True
        return result

        
s=Solution()
result= s.printZMatrix([
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
])
print(type(result))
print(result)
