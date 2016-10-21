class Mouse:
    pass

class Solution:
    mouse=Mouse()
    # @return: The same instance of this class every time
    #你的任务是设计一个 getInstance 方法
    #对于给定的类，每次调用 getInstance 时，都可得到同一个实例。
    @classmethod
    def getInstance(cls):
        # write your code here
        return cls.mouse
s=Solution()
result= s.getInstance()
print(type(result))
print(result)
s2=Solution()
result= s2.getInstance()
print(type(result))
print(result)
