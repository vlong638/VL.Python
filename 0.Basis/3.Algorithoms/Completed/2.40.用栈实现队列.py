class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        temp2=[]
        while len(self.stack2)>0:
            temp2.append(self.stack2.pop())
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        while len(temp2)>0:
            self.stack2.append(temp2.pop())
        
    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.adjust()
        return self.stack2[len(self.stack2)-1]
        
    def pop(self):
        self.adjust()
        return self.stack2.pop()
s=MyQueue()    
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.pop())
print(s.pop())
print(s.push(6))
print(s.push(7))
print(s.push(8))
print(s.push(9))
print(s.pop())
print(s.pop())
