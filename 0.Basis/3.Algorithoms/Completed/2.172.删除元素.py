class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。
    元素的顺序可以改变，并且对新的数组不会有影响。
    """
    def removeElement(self, A, elem):
        # write your code here
        i=len(A)-1
        while i>=0:
            if A[i]==elem:
                print("A.remove",A[i])
                A.remove(A[i])
                print("A:",A)
            i-=1
        return len(A)
        

    #for指针形式进行删除,则会遗漏遇二漏一
    def removeElement2(self, A, elem):
        for a in A:
            if a==elem:
                print("A.remove",a)
                print("id(a)",id(a))
                A.remove(a)
                print("A:",A)
        return len(A)


        
s=Solution()
result= s.removeElement([0,4,4,0,0,2,4,4],4)
print(type(result))
print(result)
result= s.removeElement([1,2,3,4], 5)
print(type(result))
print(result)
