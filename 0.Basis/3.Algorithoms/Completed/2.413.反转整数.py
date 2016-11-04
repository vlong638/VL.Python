class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    """
    将一个整数中的数字进行颠倒，
    当颠倒后的整数溢出时，
    返回 0 (标记为 32 位整数)。
    """
    def reverseInteger(self, n):
        # Write your code here
        #构建翻转的整数
        s=str(n)
        result=[]
        if n<0:
            s=s[1:]
        for letter in s:
            result.insert(0,letter)
        if n<0:
            result.insert(0,"-")
        else:
            result.insert(0,"+")
        #溢出检测
        maxLength=len(str(2**31))
        if len(result)>maxLength:
            print("len(result)>maxLength",len(result),">",maxLength)
            return 0
        elif len(result)==maxLength:
            if n<0:
                maxValue=str(2**31)[2:]
            else:
                maxValue=str(2**31-1)[2:]
            index=1
            while index<=maxLength:
                if result[index]>maxValue[index]:
                    print("result[index]>maxValue[index]",result[index],">",maxValue[index])
                    return 0
                else:
                    index+=1
                    print("result[index]<=maxValue[index]",result[index],"<=",maxValue[index])
        
        return int("".join(result))
            

        
s=Solution()
result= s.reverseInteger(1123)
print(type(result))
print(result)
result= s.reverseInteger(-1123)
print(type(result))
print(result)
result= s.reverseInteger(1534236469)
print(type(result))
print(result)

