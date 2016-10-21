class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, nums, target):
        # write you code here
        if len(nums)==0:
            return False        
        start=0
        end=len(nums)-1
        print("-----------search for row")
        row= self.searchMatrixForRow(nums,target,start,end)
        end=len(row)-1
        if row!=None:
            print("-----------search for value")
            return self.searchMatrixInRow(row,target,start,end)

        
    def searchMatrixForRow(self, nums, target,start,end):
        print("check range{}-{}".format(start,end))
        # write your code here
        if start==end:
            return nums[start];
        index=int((start+end)/2)
        if nums[index][0]==target:
            print("find it,at index:",index)
            return [nums[index][0]]
        elif nums[index][0]>target:
            if index-1<start:
                print("reach boundary,start:{},index:{}".format(index,start))
                return None;
            print("less than medium:{}".format(nums[index]))
            return self.searchMatrixForRow(nums,target,start,index-1)
        else:
            if index+1>end:
                print("reach boundary,index:{},end:{}".format(index,end))
                return None;
            if nums[index+1][0]>target:
                print("find it,at index:",index)
                return nums[index]
            print("great than medium:{}".format(nums[index]))
            return self.searchMatrixForRow(nums,target,index+1,end)
        
    def searchMatrixInRow(self, nums, target,start,end):
        print("check range{}-{}".format(start,end))
        # write your code here
        index=int((start+end)/2)
        print("value is ",nums[index])
        if nums[index]==target:
            print("find it,at index:",index)
            while index>1 and nums[index-1]==target:
                print("move forward")
                index-=1
            print("return",index)
            return True
        elif nums[index]>target:
            if index-1<start:
                print("reach boundary,start:{},index:{}".format(index,start))
                return False;
            print("less than medium:{}".format(nums[index]))
            return self.searchMatrixInRow(nums,target,start,index-1)
        else:
            if index+1>end:
                print("reach boundary,index:{},end:{}".format(index,end))
                return False;
            print("great than medium:{}".format(nums[index]))
            return self.searchMatrixInRow(nums,target,index+1,end)

        
s=Solution()
result= s.searchMatrix([[1,8,15,22,29,35,37,39,44,50,57,60,61,62,69,70,71,78,80]
                        ,[96,113,137,150,162,183,193,203,222,243,255,279,301,312,324,344,359,381,397]
                        ,[407,417,428,453,469,482,498,521,537,553,564,575,592,613,634,658,675,693,714]
                        ,[738,761,775,785,795,812,833,850,868,890,910,934,955,966,976,996,1014,1037,1052]
                        ,[1073,1085,1096,1121,1135,1159,1182,1196,1210,1221,1241,1262,1279,1298,1318,1330,1347,1365,1386]
                        ,[1398,1423,1444,1459,1483,1507,1517,1528,1542,1558,1568,1583,1605,1630,1641,1651,1665,1690,1714]], 80)
print(type(result))
print(result)
