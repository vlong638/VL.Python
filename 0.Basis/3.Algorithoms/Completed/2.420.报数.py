"""
报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：

1, 11, 21, 1211, 111221, ...

1 读作 "one 1" -> 11.

11 读作 "two 1s" -> 21.

21 读作 "one 2, then one 1" -> 1211.

给定一个整数 n, 返回 第 n 个顺序。

 注意事项

整数的顺序将表示为一个字符串。
"""
class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        #获取报数值
        #报数
        return self.getNumber(n)

    def getNumber(self,n):
        if n==1:
            return 1
        else:
            value=str(self.getNumber(n-1))
            if value=="1":
                return 11
            index=0
            count=1
            result=[]
            while index<len(value)-1:
                if value[index]==value[index+1]:
                    count+=1
                    index+=1
                else:
                    result.append(str(count)+str(value[index]))
                    count=1
                    index+=1
            result.append(str(count)+str(value[index]))
            print(result)
            return int("".join(result))
            
            
s=Solution()

for x in range(1,10):
    print(s.countAndSay(x))
    print()
