"""
给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。
"""
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    #动态规划非递归形式,优化空间使用
    def isInterleave1(self, s1, s2, s3):
        #边界
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1)+len(s2)!=len(s3):
            return False
        #构建动态地图+1为了[]预留空间
        #interleave[i1+1,0]记录s1
        #记录每一步的结果于interleave[i1+1,i2+1]
        interleave = [[False] * (len(s2) + 1)
                      for i in range(len(s1) + 1)]
        interleave[0][0] = True    
        for i in range(len(s1)):
            print(i + 1,0,s1[:i + 1],s3[:i + 1])
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
        self.display(interleave)
        for i in range(len(s1)):
            for j in range(len(s2)):
                #走s1
                if s1[i] == s3[i + j + 1]:
                    print("s1")
                    print("interleave[i + 1][j + 1]=",i + 1,j + 1,interleave[i][j + 1])
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                #走s2
                if s2[j] == s3[i + j + 1]:
                    print("s2")
                    print("interleave[i + 1][j + 1]=",i + 1,j + 1,interleave[i+1][j + 1])
                    print("interleave[i + 1][j]=",i + 1,j ,interleave[i + 1][j])
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]    
        return interleave[len(s1)][len(s2)]

    def display(self,s):
        print("display---------")
        for letter in s:
            print(letter)
        print("display---------")
    
    """
方案一 没有足够顾及单边空的情况
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                interleave[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]
方案二
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
            for j in range(len(s2)):
                interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
                interleave[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]

    """
    
    #动态规划 递归形式,空间消耗较高
    def isInterleave2(self, s1, s2, s3):
        #边界
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1)+len(s2)!=len(s3):
            return False

        return self.isInterleaveDynamic(s1, s2, s3)
        
    def isInterleaveDynamic(self, s1, s2, s3):
        if len(s1)==0:
            return s3==s2
        elif len(s2)==0:
            return s3==s1
        if s1[0]==s2[0] and s1[0]==s3[0]:
            return self.isInterleaveDynamic(s1[1:], s2, s3[1:]) or self.isInterleaveDynamic(s1, s2[1:], s3[1:])
        elif s1[0]==s3[0]:
            return self.isInterleaveDynamic(s1[1:], s2, s3[1:])
        elif s2[0]==s3[0]:
            return self.isInterleaveDynamic(s1, s2[1:], s3[1:])
        else:
            return False

s=Solution()
result= s.isInterleave1("aadbbcadbbcabcccc","dbbcadbbca","aadbbdbbcadbbcacbcacccdbbca")
print(result)
"""
import datetime
t1=datetime.datetime.now()
result= s.isInterleave1("aadbbcadbbcabcccc","dbbcadbbca","aadbbdbbcadbbcacbcacccdbbca")
print(result)
result= s.isInterleave1("aabcccc","dbbca","aadbbbaccccc")
print(result)
t2=datetime.datetime.now()
t3=datetime.datetime.now()
result= s.isInterleave2("aadbbcadbbcabcccc","dbbcadbbca","aadbbdbbcadbbcacbcacccdbbca")
print(result)
result= s.isInterleave2("aabcccc","dbbca","aadbbbaccccc")
print(result)
t4=datetime.datetime.now()
print("static   ",t2-t1)
print("recursive",t4-t3)
"""
