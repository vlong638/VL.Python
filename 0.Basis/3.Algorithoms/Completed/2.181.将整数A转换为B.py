class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    """
            print("a",bin(a))
            print("b",bin(b))
            print("a^b",bin(a^b))
    如果要将整数A转换为B，需要改变多少个bit位？
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        print()
        print("a",a,bin(a))
        print("b",b,bin(b))
        count=0
        #求状态位差异,并将特殊位置为0
        if a>=0 and b>=0:
            pass
        elif a>0:
            count+=1
            if b==-2147483648:
                print("b=0")
                b=0
        elif b>0:
            count+=1
            if a==-2147483648:
                print("a=0")
                a=0
        else:
            pass
        #对将显示的原码转为机器存储的反码
        if a>=0 and b>=0:
            pass
        elif a>0:
            b-=1
            b=~b
            length=len(bin(b))-2
            b+=2**31-2**length
        elif b>0:
            a-=1
            a=~a
            length=len(bin(a))-2
            a+=2**31-2**length
        else:
            pass
        #求位变化个数
        print("=>")
        print("a",a,bin(a))
        print("b",b,bin(b))
        print("a^b",bin(a^b))
        for letter in bin(a^b):
            if letter=="1":
                count+=1
        return count


    """
        count=0
        
        if a<0 or b<0:
            if a<0:
                a=~a

            
            count=32
            for letter in bin(a&b):
                print(letter,end=" ")
                if letter=="1":
                    count-=1
            print()
            return count
        print("差异:",end="")
        for letter in bin(a^b):
            print(letter,end=" ")
            if letter=="1":
                count+=1
        print()
        return count
    """

     
s=Solution()
result= s.bitSwapRequired(14,31)
print(result)
result= s.bitSwapRequired(-1,1)
print(result)
result= s.bitSwapRequired(-2147483648, 2147483647)
print(result)
result= s.bitSwapRequired(-64, 32)
print(result)


"""
关于树的处理辅助
import Displayer
dis=Displayer.Displayer()
dis.DisplayTree(dis.SampleTree)
"""
