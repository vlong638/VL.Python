import PrintHelper
class Solution:
#@param A and B: sorted integer array A and B.
#@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        c=[]
        while len(A)>0:
            if len(B)==0:
                break
            elif A[len(A)-1]>B[len(B)-1]:
                c.append(A.pop())
            else:
                c.append(B.pop())
        while len(A)>0:
            c.append(A.pop())
        while len(B)>0:
            c.append(B.pop())
        result=[]
        while len(c)>0:
            result.append(c.pop())
        return result

            
    def mergeSortedArray2(self, A, B):
        # write your code here
        c=[]
        a=None
        b=None
        while len(A)>0:
            if a==None:
                a=A.pop(0)
            if len(B)==0:
                c.append(a)
                print("append",a)
                c.extend(A)
                print("extend",A)
                break
            elif b==None:
                b=B.pop(0)
            print(a,b)
            if a>b:
                c.append(b)
                print("append",b)
                b=None
            else:
                c.append(a)
                print("append",a)
                a=None
        if a!=None:
            c.append(a)
            print("append",a)
        if b!=None:
            c.append(b)
            print("append",b)
        if len(B)>0:
            c.extend(B)
            print("extend",B)
        return c
PrintHelper.PrintCode('s=Solution()')
PrintHelper.PrintCode('c=s.mergeSortedArray([1,2,3,3,4,5],[1,4,5,7])')
PrintHelper.PrintCode('print(c)')
s=Solution()
c=s.mergeSortedArray([1,2,3,3,4,5],[1,4,5,7])
print(c)

c=s.mergeSortedArray([1,5], [2,3])
print(c)
