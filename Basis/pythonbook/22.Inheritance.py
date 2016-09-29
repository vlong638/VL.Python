import PrintHelper
PrintHelper.PrintTitle('Class Inheritance,继承')
PrintHelper.PrintHint('pass,用以省略实现')
PrintHelper.PrintCode('class Person:')
PrintHelper.PrintCode('    def __init__( self, firstname, lastname, age ):')
PrintHelper.PrintCode('        self.firstname = firstname')
PrintHelper.PrintCode('        self.lastname = lastname')
PrintHelper.PrintCode('        self.age = age')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"{} {}\".format( self.firstname, self.lastname )')
PrintHelper.PrintCode('    def underage( self ):')
PrintHelper.PrintCode('        return self.age < 18')
PrintHelper.PrintCode('class Student( Person ):')
PrintHelper.PrintCode('    pass')
class Person:
    def __init__( self, firstname, lastname, age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__( self ):
        return "{} {}".format( self.firstname, self.lastname )
    def underage( self ):
        return self.age < 18
class Student( Person ):
    pass
PrintHelper.PrintCode('albert = Student( \"Albert\", \"Applebaum\", 19 )')
albert = Student( "Albert", "Applebaum", 19 )
PrintHelper.PrintCode('print( albert )')
print( albert )
PrintHelper.PrintCode('print( albert.underage() )')
print( albert.underage() )
PrintHelper.PrintSubtitle('Extending and Overriding,扩展和重写')
print('定义父类已存在的方法,则会覆盖该方法的实现.')
print('如果希望重写的过程中依旧调用父类的方法,则可以使用关键字super()')
PrintHelper.PrintHint('super()')
PrintHelper.PrintCode('class Person:')
PrintHelper.PrintCode('    def __init__( self, firstname, lastname, age ):')
PrintHelper.PrintCode('        self.firstname = firstname')
PrintHelper.PrintCode('        self.lastname = lastname')
PrintHelper.PrintCode('        self.age = age')
PrintHelper.PrintCode('    def __repr__( self ):')
PrintHelper.PrintCode('        return \"{} {}\".format( self.firstname, self.lastname )')
PrintHelper.PrintCode('    def underage( self ):')
PrintHelper.PrintCode('        return self.age < 18')
PrintHelper.PrintCode('class Student( Person ):')
PrintHelper.PrintCode('    def __init__( self, firstname, lastname, age, program ):')
PrintHelper.PrintCode('        super().__init__( firstname, lastname, age )')
PrintHelper.PrintCode('        self.courselist = []')
PrintHelper.PrintCode('        self.program = program')
PrintHelper.PrintCode('    def underage( self ):')
PrintHelper.PrintCode('        return self.age < 21')
PrintHelper.PrintCode('    def enroll( self, course ):')
PrintHelper.PrintCode('        self.courselist.append( course )')
class Person:
    def __init__( self, firstname, lastname, age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__( self ):
        return "{} {}".format( self.firstname, self.lastname )
    def underage( self ):
        return self.age < 18
class Student( Person ):
    def __init__( self, firstname, lastname, age, program ):
        super().__init__( firstname, lastname, age )
        self.courselist = []
        self.program = program
    def underage( self ):
        return self.age < 21
    def enroll( self, course ):
        self.courselist.append( course )
PrintHelper.PrintCode('albert = Student( \"Albert\", \"Applebaum\", 19, \"CSAI\" )')
albert = Student( "Albert", "Applebaum", 19, "CSAI" )
PrintHelper.PrintCode('print( albert )')
print( albert )
PrintHelper.PrintCode('print( albert.underage() )')
print( albert.underage() )
PrintHelper.PrintCode('print( albert.program )')
print( albert.program )
PrintHelper.PrintCode('albert.enroll( \"Methods of Rationality\" )')
albert.enroll( "Methods of Rationality" )
PrintHelper.PrintCode('albert.enroll')
albert.enroll
PrintHelper.PrintCode('( \"Defense Against the Dark Arts\" )')
( "Defense Against the Dark Arts" )
PrintHelper.PrintCode('print( albert.courselist )')
print( albert.courselist )
PrintHelper.PrintSubtitle('Multiple Inheritance,多继承')
print('Python支持多重继承')
print('假如类被定义成这种形式Class D(A,B,C)')
print('你希望在__init__()中调用父类的方法')
print('可以用这种形式A.__init(),B.__init(),C.__init()')
PrintHelper.PrintHint('Parent.__init__(self[,@parameter])')
PrintHelper.PrintCode('class A:')
PrintHelper.PrintCode('    def __init__(self,name):')
PrintHelper.PrintCode('        self.Name=name')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return self.Name')
PrintHelper.PrintCode('class B:')
PrintHelper.PrintCode('    def __init__(self,age):')
PrintHelper.PrintCode('        self.Age=age')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return self.Age')
PrintHelper.PrintCode('class C:')
PrintHelper.PrintCode('    def __init__(self,sex):')
PrintHelper.PrintCode('        self.Sex=sex')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return self.Sex')
PrintHelper.PrintCode('class D(A,B,C):')
PrintHelper.PrintCode('    def __init__(self,name,age,sex):')
PrintHelper.PrintCode('        A.__init__(self,name)')
PrintHelper.PrintCode('        B.__init__(self,age)')
PrintHelper.PrintCode('        C.__init__(self,sex)')
PrintHelper.PrintCode('    def __repr__(self):')
PrintHelper.PrintCode('        return \"Name:{},Age:{},Sex:{}\".format(self.Name,self.Age,self.Sex)')
class A:
    def __init__(self,name):
        self.Name=name
    def __repr__(self):
        return self.Name
class B:
    def __init__(self,age):
        self.Age=age
    def __repr__(self):
        return self.Age
class C:
    def __init__(self,sex):
        self.Sex=sex
    def __repr__(self):
        return self.Sex
class D(A,B,C):
    def __init__(self,name,age,sex):
        A.__init__(self,name)
        B.__init__(self,age)
        C.__init__(self,sex)
    def __repr__(self):
        return "Name:{},Age:{},Sex:{}".format(self.Name,self.Age,self.Sex)
PrintHelper.PrintCode('d=D(\'xjh\',26,\'man\')')
d=D('xjh',26,'man')
PrintHelper.PrintCode('print(repr(d))')
print(repr(d))
PrintHelper.PrintTitle('Interfaces')
print('接口是用来声明属性和方法但是并不予以实现的一个类')
print('由于其子类会将其予以实现,所以可以像操作实现的类一样操作他们.')
PrintHelper.PrintHint('NotImplemented,未实现')
PrintHelper.PrintCode('class Vehicle:')
PrintHelper.PrintCode('    def __init__(self):')
PrintHelper.PrintCode('        self.startpiont=[]')
PrintHelper.PrintCode('        self.endpoints=[]')
PrintHelper.PrintCode('        self.verb=\"\"')
PrintHelper.PrintCode('        self.name=\"\"')
PrintHelper.PrintCode('    def __str__(self):')
PrintHelper.PrintCode('        return self.name')
PrintHelper.PrintCode('    def isStartpoint(self,p):')
PrintHelper.PrintCode('        return NotImplemented')
PrintHelper.PrintCode('    def isEndpoint(self,p):')
PrintHelper.PrintCode('        return NotImplemented')
PrintHelper.PrintCode('    def travel_speed(self,p1,p2):')
PrintHelper.PrintCode('        return NotImplemented')
PrintHelper.PrintCode('    def travelVerb(self):')
PrintHelper.PrintCode('        return NotImplemented')
class Vehicle:
    def __init__(self):
        self.startpiont=[]
        self.endpoints=[]
        self.verb=""
        self.name=""
    def __str__(self):
        return self.name
    def isStartpoint(self,p):
        return NotImplemented
    def isEndpoint(self,p):
        return NotImplemented
    def travel_speed(self,p1,p2):
        return NotImplemented
    def travelVerb(self):
        return NotImplemented






















