"""
给定一个整数数组来表示排列，找出其上一个排列。

 注意事项

排列中可能包含重复的整数
"""
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        print()
        i=len(num)-1
        while i>=0:
            j=len(num)-1
            while j>0 and j>i:
                if num[j]<num[i]:
                    print("change {} and {}".format(num[i],num[j]))
                    print("i {} j {}".format(i,j))
                    result=[]
                    if i-1>=0:
                        print("result.extend(num[0:i])",num[0:i])
                        result.extend(num[0:i])
                    result.append(num[j])
                    print("result.append(num[0:j])",num[j])
                    partB=[]
                    if i+1<=j-1:
                        partB.extend(num[i+1:j])
                        print("partB.extend(num[i+1:j])",num[i+1:j])
                    partB.append(num[i])
                    print("partB.append(num[i])",num[i])
                    if j+1<=len(num)-1:
                        partB.extend(num[j+1:])
                        print("partB.extend(num[j+1:].sort())",num[j+1:].sort())
                    partB.sort(reverse=True)
                    result.extend(partB)
                    return result
                j-=1
            i-=1
        print("reverse")
        num.sort(reverse=True)
        return num

s=Solution()
print(s.previousPermuation([1,3,2,3]))
