"""
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
"""
class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self,matrix,target):
        print()
        print("search------------")
        for line in matrix:
            print(line)
        print("for",target)
        print()


        
        self.result=0
        if matrix!=None and len(matrix[0])>0:
            self.searchMatrixByMap(matrix,target,0,len(matrix[0])-1)
        return self.result
        
    def searchMatrixByMap(self, matrix, target,y,x):
        if len(matrix)==0:
            return 0
        #行内查找target 遍历可以改为快排
        if matrix[y][x]>=target:
            x=self.searchMatrixInRow(matrix[y],target,0,x)
            """
            while x>0 and matrix[y][x-1]>=target:
                print("move pre, matrix[y][x-1]:",matrix[y][x-1])
                x-=1
            """
            if matrix[y][x]==target:
                print("find at y:{},x:{} ".format(y,x))
                self.result+=1
                
        if y<len(matrix)-1 and matrix[y+1][0]<=target:
            print("check next y:",y+1,"x:",x)
            self.searchMatrixByMap(matrix, target,y+1,x)
            
            
    def searchMatrixInRow(self, nums, target,start,end):
        print("check range{}-{}".format(start,end))
        # write your code here
        index=int((start+end)/2)
        print("value is ",nums[index])
        if nums[index]==target:
            print("find it,at index:",index)
            return index
        elif nums[index]>target:
            if index-1<start:
                print("reach boundary,start:{},index:{}".format(index,start))
                return index
            print("less than medium:{}".format(nums[index]))
            return self.searchMatrixInRow(nums,target,start,index-1)
        else:
            if index+1>end:
                print("reach boundary,index:{},end:{}".format(index,end))
                return end;
            print("great than medium:{}".format(nums[index]))
            return self.searchMatrixInRow(nums,target,index+1,end)

s=Solution()
result= s.searchMatrix([

    [1, 3, 5, 7],

    [2, 4, 7, 8],

    [3, 5, 9, 10]

],3)
print(result)

result= s.searchMatrix([[5]],3)
print(result)

result= s.searchMatrix([[52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88],[53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89],[54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90],[55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91],[56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92],[57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93]], 71)
print(result)
