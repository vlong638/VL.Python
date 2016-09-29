import PrintHelper
PrintHelper.PrintTitle('Object Orientation,面向对象','Structured Programming,结构化编程','Imperative Programming,命令式编程')
PrintHelper.PrintSubtitle('The Object Oriented World')
print('略')
PrintHelper.PrintSubtitle('Students,Teachers,Courses')
print('示例.略')
PrintHelper.PrintSubtitle('Classes,Objects,Hierarchies')
PrintHelper.PrintSubtitle('Classes And Data Types In Python')
print('你会发现方法总是以@variable.@method的形式被调用')
print('而你对string进行操作的时候,则如@string.lower(),这里表明了string就是class的一个实例')
print('同样的,integers,floats等等都是class的实例')
PrintHelper.PrintTitle('Classes And Objects')
PrintHelper.PrintHint('class')
print('class可以被视作一种数据类型,一旦创建,就可以给参数赋予这种类型')
print('pass关键字意味着这个类没有做任何事,你需要实现一些语句或者需要pass')
PrintHelper.PrintHint('pass关键字')
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    pass')
class Point:
    pass
PrintHelper.PrintHint('__init__(),构造函数'
                      ,"self的使用有些类似C#扩展方法中的this,当然你可以不用self,它并不是一个关键字")
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__(self):')
PrintHelper.PrintCode('        self.x=0.1')
PrintHelper.PrintCode('        self.y=0.2')
PrintHelper.PrintCode('        ')
PrintHelper.PrintCode('p=Point()')
PrintHelper.PrintCode('p.z=0.3')
PrintHelper.PrintCode('print(\"x:{},y:{},z:{}\".format(p.x,p.y,p.z))')
class Point:
    def __init__(selfb):
        selfb.x=0.1
        selfb.y=0.2
        
p=Point()
p.z=0.3
print("x:{},y:{},z:{}".format(p.x,p.y,p.z))
PrintHelper.PrintHint('__repr__(),缩写 of Represent')
PrintHelper.PrintCode('print(p)')
print(p)
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__(self,x=0.1,y=0.2):')
PrintHelper.PrintCode('        self.x=x')
PrintHelper.PrintCode('        self.y=y')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return (\"x:{},y:{}\".format(p.x,p.y))')
PrintHelper.PrintCode('p=Point(3.5,5.0)')
PrintHelper.PrintCode('print(p)')
class Point:
    def __init__(self,x=0.1,y=0.2):
        self.x=x
        self.y=y
    def __repr__(self):
        return ("x:{},y:{}".format(p.x,p.y))
p=Point(3.5,5.0)
print(p)
PrintHelper.PrintHint('__str__()','__str__()方法和__repr__()方法相似,但是它只对print()有效')
print('这里重点解释一些str和repr的区别')
print('repr将对象转换成编译期可识别的形式')
print('而str则将对象转成人类可读的字符串形式')
print('当这两种形式没有明显差异的情况下,两者可以返回相同的东西')
print('repr是建议总是实现的,而str则是可选的')
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__(self,x=0.1,y=0.2):')
PrintHelper.PrintCode('        self.x=x')
PrintHelper.PrintCode('        self.y=y')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return (\"x:{},y:{}\".format(p.x,p.y))')
PrintHelper.PrintCode('    def __str__(self):')
PrintHelper.PrintCode('        return (\"I am a point\")')
class Point:
    def __init__(self,x=0.1,y=0.2):
        self.x=x
        self.y=y
    def __repr__(self):
        return ("x:{},y:{}".format(p.x,p.y))
    def __str__(self):
        return ("I am a point")
PrintHelper.PrintCode('p=Point(3.5,5.0)')
p=Point(3.5,5.0)
PrintHelper.PrintCode('print(p)')
print(p)
PrintHelper.PrintCode('print(str(p))')
print(str(p))
PrintHelper.PrintCode('print(repr(p))')
print(repr(p))
PrintHelper.PrintTitle('Methods')
print('定义方法样例')
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__( self, x=0.0, y=0.0 ):')
PrintHelper.PrintCode('        self.x = x')
PrintHelper.PrintCode('        self.y = y')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"({}, {})\".format( self.x, self.y )')
PrintHelper.PrintCode('    def Translate( self, shift_x, shift_y ):')
PrintHelper.PrintCode('        self.x += shift_x')
PrintHelper.PrintCode('        self.y += shift_y')
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def Translate( self, shift_x, shift_y ):
        self.x += shift_x
        self.y += shift_y
PrintHelper.PrintCode('p=Poitn(1,2)')
p=Point(1,2)
PrintHelper.PrintCode('print(p)')
print(p)
PrintHelper.PrintCode('p.Translate(-3,7)')
p.Translate(-3,7)
PrintHelper.PrintCode('print(p)')
print(p)
PrintHelper.PrintTitle('Nesting Objects,内置对象')
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__( self, x=0.0, y=0.0 ):')
PrintHelper.PrintCode('        self.x = x')
PrintHelper.PrintCode('        self.y = y')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"({}, {})\".format( self.x, self.y )')
PrintHelper.PrintCode('class Rectangle:')
PrintHelper.PrintCode('    def __init__( self, point, width, height ):')
PrintHelper.PrintCode('        self.point = point')
PrintHelper.PrintCode('        self.width = width')
PrintHelper.PrintCode('        self.height = height')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"[{},w={},h={}]\".format( self.point, self.width, self.height )')
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
class Rectangle:
    def __init__( self, point, width, height ):
        self.point = point
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, self.height )
PrintHelper.PrintCode('p = Point( 3.5, 5.0 )')
p = Point( 3.5, 5.0 )
PrintHelper.PrintCode('r = Rectangle( p, 4.0, 2.0 )')
r = Rectangle( p, 4.0, 2.0 )
PrintHelper.PrintCode('print( r )')
print( r )
PrintHelper.PrintSubtitle('Copies And References')
print('内置类的使用默认是以引用存储的')
print('可以使用copy()来创建独立副本')
PrintHelper.PrintCode('from copy import copy')
PrintHelper.PrintCode('class Point:')
PrintHelper.PrintCode('    def __init__( self, x=0.0, y=0.0 ):')
PrintHelper.PrintCode('        self.x = x')
PrintHelper.PrintCode('        self.y = y')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"({}, {})\".format( self.x, self.y )')
PrintHelper.PrintCode('class Rectangle:')
PrintHelper.PrintCode('    def __init__( self, point, width, height ):')
PrintHelper.PrintCode('        self.point = point')
PrintHelper.PrintCode('        self.pointCopy = copy(point)')
PrintHelper.PrintCode('        self.width = width')
PrintHelper.PrintCode('        self.height = height')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"[pointOrient:{},pointCopy:{},w={},h={}]\".format( self.point, self.pointCopy, self.width, self.height )')
from copy import copy
class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
class Rectangle:
    def __init__( self, point, width, height ):
        self.point = point
        self.pointCopy = copy(point)
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[pointOrient:{},pointCopy:{},w={},h={}]".format( self.point, self.pointCopy, self.width, self.height )
PrintHelper.PrintCode('p=Point( 3.5, 5.0 )')
p=Point( 3.5, 5.0 )
PrintHelper.PrintCode('r=Rectangle( p, 4.0, 2.0 )')
r=Rectangle( p, 4.0, 2.0 )
PrintHelper.PrintCode('print(r)')
print(r)
PrintHelper.PrintCode('p.x=10')
p.x=10
PrintHelper.PrintCode('p.y=20')
p.y=20
PrintHelper.PrintCode('print(r)')
print(r)
