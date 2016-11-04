import PrintHelper
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode(' \"\"\"')
PrintHelper.PrintCode(' @param a: The first integer')
PrintHelper.PrintCode(' @param b: The second integer')
PrintHelper.PrintCode(' @return: The sum of a and b')
PrintHelper.PrintCode(' \"\"\"')
PrintHelper.PrintCode(' def aplusb(self, a, b):')
PrintHelper.PrintCode('     if a==0:')
PrintHelper.PrintCode('         return b')
PrintHelper.PrintCode('     if b==0:')
PrintHelper.PrintCode('         return a')
PrintHelper.PrintCode('     c=a^b')
PrintHelper.PrintCode('     d=(a&b)<<1;')
PrintHelper.PrintCode('     print(\"c\",bin(c))')
PrintHelper.PrintCode('     print(\"d\",bin(d))')
PrintHelper.PrintCode('     return self.aplusb(c,d)')
PrintHelper.PrintCode('    ')
PrintHelper.PrintCode(' def DisplayAB(self, a, b):')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"a\",bin(a)))')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"b\",bin(b)))')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"a+b\",bin(a+b)))')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"a&b\",bin(a&b)))')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"a|b\",bin(a|b)))')
PrintHelper.PrintCode('     print(\"{:5}{:>10}\".format(\"a^b\",bin(a^b)))')

    
"""
@param a: The first integer
@param b: The second integer
@return: The sum of a and b
"""
class Solution:
    def aplusb(self, a, b):
        if a==0:
            return b
        if b==0:
            return a
        c=a^b
        d=(a&b)<<1;
        if c==-2**32:
            return 0
        print("a     ","{:>10}".format(bin(a)))
        print("b     ","{:>10}".format(bin(b)))
        print("a^b   ","{:>10}".format(bin(c)))
        print("a&b<<1","{:>10}".format(bin(d)))
        print()
        return self.aplusb(c,d)
    
    def DisplayAB(self, a, b):
        print("{:5}{:>10}".format("a",bin(a)))
        print("{:5}{:>10}".format("b",bin(b)))
        print("{:5}{:>10}".format("a+b",bin(a+b)))
        print("{:5}{:>10}".format("a&b",bin(a&b)))
        print("{:5}{:>10}".format("a|b",bin(a|b)))
        print("{:5}{:>10}".format("a^b",bin(a^b)))

print('bin(integer)获取二进制表示')
PrintHelper.PrintCode('a=11')
PrintHelper.PrintCode('print(bin(a))')
PrintHelper.PrintCode('print()')
a=11
print(bin(a))
print()
PrintHelper.PrintCode('print(len(bin(a)))')
PrintHelper.PrintCode('print()')
print(len(bin(a)))
print()
PrintHelper.PrintCode('for letter in bin(a):')
PrintHelper.PrintCode('    print(letter)')
PrintHelper.PrintCode('print()')
for letter in bin(a):
    print(letter)
print()
PrintHelper.PrintCode('s=Solution()')
PrintHelper.PrintCode('s.DisplayAB(43,57)')
PrintHelper.PrintCode('print()')
PrintHelper.PrintCode('print(s.aplusb(43,57))')
s=Solution()
s.DisplayAB(43,57)
print()
print('位的几类运算')
print('& 求同')
print('| 求高位和')
print('^ 求差异')
print('对整数求和的位运算过程可以拆分为')
print('1.求非进位部分,非进位部分直接相加,非进位部分为a^b,即差异部分')
print('2.求进位部分,进位部分为两者的重叠即a&b<<1.')
print('作一个简单例子11和01,差异部分10,进位部分为01<<1,即10')
print('差异和进位依旧是两个值')
print('继续重复差异和进位处理,直到某部分为0')
print(s.aplusb(43,57))
print(s.aplusb(100,-100))
