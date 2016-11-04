"""
给一组整数，按照升序排序。使用归并排序，快速排序，堆排序
或者任何其他 O(n log n) 的排序算法。
"""
import pdb
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        #快排
        length=len(A)
        if length==0:
            return []
        elif length==1:
            return A
        #取中位,分左右区间
        mediumIndex=int(length/2)
        medium=A.pop(mediumIndex)
        length-=1
        pre=[]
        end=[]
        index=0
        while index<length:
            if A[index]<medium:
                pre.append(A[index])
            else:
                end.append(A[index])
            index+=1
        #平衡化
        if len(end)==0:
            end.append(medium)
        else:
            pre.append(medium)
        print("medium",medium)
        print("pre",pre)
        print("end",end)
        #连接左右区间
        if len(pre)>1:
            pre=self.sortIntegers2(pre)
        if len(end)>1:
            end=self.sortIntegers2(end)
        #return
        print("medium",medium)
        print("pre",pre)
        print("end",end)
        if pre==None:
            return end
        elif end==None:
            return pre
        else:
            pre.extend(end)
            return pre


s=Solution()
result= s.sortIntegers2([3, 2, 1, 4, 5])
print(type(result))
print(result)
