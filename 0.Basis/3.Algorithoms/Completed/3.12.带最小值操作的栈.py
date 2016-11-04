"""
实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。

你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。

 注意事项

如果堆栈中没有数字则不能进行min方法的调用

==>
push()后进先出
后进的最小值总是上一个中最小的...
"""
class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.Stack=[]
        self.MinStack=[]

    def push(self, number):
        # write yout code here
        self.Stack.append(number)
        if len(self.MinStack)==0 or self.MinStack[-1]>=number:
            self.MinStack.append(number)
        

    def pop(self):
        # pop and return the top item in stack
        if self.Stack[-1]==self.MinStack[-1]:
            self.MinStack.pop()
        return self.Stack.pop()

    def min(self):
        # return the minimum number in stack
        return self.MinStack[-1]
  
    
s=MinStack()
result= s.push(11)
result= s.push(12)
result= s.push(13)
result= s.push(14)
result= s.push(15)
result= s.push(5)
result= s.push(6)
result= s.push(1)
result= s.push(2)

print("min",s.min())
print()
print("pop",s.pop())
print("min",s.min())
print()
print("pop",s.pop())
print("min",s.min())
print()
print("pop",s.pop())
print("min",s.min())
print()
print("pop",s.pop())
print("min",s.min())

