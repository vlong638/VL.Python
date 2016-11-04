"""
工厂模式是一种常见的设计模式。
请实现一个玩具工厂 ToyFactory 用来产生不同的玩具类。
可以假设只有猫和狗两种玩具。
"""
"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print("Wow")

class Cat(Toy):
    # Write your code here
    def talk(self):
        print("Meow")


class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        # Write your code here
        if type=="Dog":
            return Dog()
        if type=="Cat":
            return Cat()



        
s=Solution()
result= s.rotateString("abcd123456789",2)
print(type(result))
print(result)
