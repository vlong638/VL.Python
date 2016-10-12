import PrintHelper
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode('#@param A and B: sorted integer array A and B.')
PrintHelper.PrintCode('#@return: A new sorted integer array')
PrintHelper.PrintCode(' def mergeSortedArray(self, A, B):')
PrintHelper.PrintCode('    # write your code here')
PrintHelper.PrintCode('    c=[]')
PrintHelper.PrintCode('    a=None')
PrintHelper.PrintCode('    b=None')
PrintHelper.PrintCode('    while len(A)>0:')
PrintHelper.PrintCode('        if a==None:')
PrintHelper.PrintCode('            a=A.pop(0)')
PrintHelper.PrintCode('        if len(B)==0:')
PrintHelper.PrintCode('            c.append(a)')
PrintHelper.PrintCode('            print(\"append\",a)')
PrintHelper.PrintCode('            c.extend(A)')
PrintHelper.PrintCode('            print(\"extend\",A)')
PrintHelper.PrintCode('            break')
PrintHelper.PrintCode('        elif b==None:')
PrintHelper.PrintCode('            b=B.pop(0)')
PrintHelper.PrintCode('        print(a,b)')
PrintHelper.PrintCode('        if a>b:')
PrintHelper.PrintCode('            c.append(b)')
PrintHelper.PrintCode('            print(\"append\",b)')
PrintHelper.PrintCode('            b=None')
PrintHelper.PrintCode('        else:')
PrintHelper.PrintCode('            c.append(a)')
PrintHelper.PrintCode('            print(\"append\",a)')
PrintHelper.PrintCode('            a=None')
PrintHelper.PrintCode('    if len(B)>0:')
PrintHelper.PrintCode('        if a!=None:')
PrintHelper.PrintCode('            c.append(a)')
PrintHelper.PrintCode('            print(\"append\",a)')
PrintHelper.PrintCode('        c.extend(B)')
PrintHelper.PrintCode('        print(\"extend\",B)')
PrintHelper.PrintCode('    if a!=None:')
PrintHelper.PrintCode('        c.append(a)')
PrintHelper.PrintCode('    if b!=None:')
PrintHelper.PrintCode('        c.append(b)')
PrintHelper.PrintCode('    return c')
class Solution:
#@param A and B: sorted integer array A and B.
#@return: A new sorted integer array
 def mergeSortedArray(self, A, B):
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
