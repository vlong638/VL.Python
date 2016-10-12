import PrintHelper
PrintHelper.PrintTitle('Interators')
PrintHelper.PrintHint('for...in...,这种命令可以被应用在多种场合')
PrintHelper.PrintSubtitle('for list,数列')
PrintHelper.PrintCode('for i in [1,2,3,4]:')
PrintHelper.PrintCode('    print(i,end=\"\")')
PrintHelper.PrintCode('print()')
for i in [1,2,3,4]:
    print(i,end="")
print()
PrintHelper.PrintSubtitle('for tuple,元组')
PrintHelper.PrintCode('for i in(\"pi\",3.14,22/7):')
PrintHelper.PrintCode('    print(i,end=\"\")')
PrintHelper.PrintCode('print()')
for i in("pi",3.14,22/7):
    print(i,end="")
print()
PrintHelper.PrintSubtitle('for range,数组')
PrintHelper.PrintCode('for i in range(3,11,2):')
PrintHelper.PrintCode('    print(i,end=\"\")')
PrintHelper.PrintCode('print()')
for i in range(3,11,2):
    print(i,end="")
print()
PrintHelper.PrintSubtitle('for string,字符串')
PrintHelper.PrintCode('for i in \"hello\":')
PrintHelper.PrintCode('    print(i,end=\"\")')
PrintHelper.PrintCode('print()')
for i in "hello":
    print(i,end="")
print()
PrintHelper.PrintSubtitle('for dictionary,字典')
PrintHelper.PrintCode('for key in {\"apple\":1,\"banana\":3}:')
PrintHelper.PrintCode('    print(key,end=\"\")')
PrintHelper.PrintCode('print()')
for key in {"apple":1,"banana":3}:
    print(key,end="")
print()
PrintHelper.PrintSubtitle('Iterable Objects,构建可迭代对象')
PrintHelper.PrintHint('__iter__()')
PrintHelper.PrintHint('__next__()')
PrintHelper.PrintCode('class Fibonacci:')
PrintHelper.PrintCode('    def __init__(self):')
PrintHelper.PrintCode('        self.sequence=[1,1,2,3,5,8,13,21,34,55]')
PrintHelper.PrintCode('    def __iter__(self):')
PrintHelper.PrintCode('        return self')
PrintHelper.PrintCode('    def __next__(self):')
PrintHelper.PrintCode('        if len(self.sequence)>0:')
PrintHelper.PrintCode('            return self.sequence.pop(0)')
PrintHelper.PrintCode('        raise StopIteration()')
PrintHelper.PrintCode('fseq=Fibonacci()')
PrintHelper.PrintCode('for n in fseq:')
PrintHelper.PrintCode('    print(n,end=\",\")')
class Fibonacci:
    def __init__(self):
        self.sequence=[1,1,2,3,5,8,13,21,34,55]
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.sequence)>0:
            return self.sequence.pop(0)
        raise StopIteration()
fseq=Fibonacci()
for n in fseq:
    print(n,end=",")
PrintHelper.PrintSubtitle('关于Fibonacci另一种更优雅的实现')
PrintHelper.PrintCode('class Fibonacci():')
PrintHelper.PrintCode('    def __init__(self):')
PrintHelper.PrintCode('        self.a, self.b = 0, 1 # 初始化两个计数器a，b')
PrintHelper.PrintCode('')
PrintHelper.PrintCode('    def __iter__(self):')
PrintHelper.PrintCode('        return self # 实例本身就是迭代对象，故返回自己')
PrintHelper.PrintCode('')
PrintHelper.PrintCode('    def next(self):')
PrintHelper.PrintCode('        self.a, self.b = self.b, self.a + self.b # 计算下一个值')
PrintHelper.PrintCode('        if self.a > 10000: # 退出循环的条件')
PrintHelper.PrintCode('            raise StopIteration();')
PrintHelper.PrintCode('        return self.a # 返回下一个值')
PrintHelper.PrintCode('for n in Fibonacci():')
PrintHelper.PrintCode('    print(n,end=",")')
class Fibonacci():
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
for n in Fibonacci():
    print(n,end=",")
PrintHelper.PrintSubtitle('Delegated Iteration,授权迭代')
print('关于授权迭代,我们可以得出一点,for...in...本质上是访问__iter__()函数')
print('并经由__iter__()函数返回调用其他对象的__next__()的结果集')
print('使用授权迭代可以让迭代不在每次结束后都需重置数据')
PrintHelper.PrintCode('class FiboIterable:')
PrintHelper.PrintCode('    def __init__( self, seq ):')
PrintHelper.PrintCode('        self.seq = seq')
PrintHelper.PrintCode('    def __next__( self ):')
PrintHelper.PrintCode('        if len( self.seq ) > 0:')
PrintHelper.PrintCode('            return self.seq.pop(0)')
PrintHelper.PrintCode('        raise StopIteration()')
PrintHelper.PrintCode('class Fibo:')
PrintHelper.PrintCode('    def __init__( self, maxnum=1000 ):')
PrintHelper.PrintCode('        self.maxnum = maxnum')
PrintHelper.PrintCode('    def __iter__( self ):')
PrintHelper.PrintCode('        nr1 = 0')
PrintHelper.PrintCode('        nr2 = 1')
PrintHelper.PrintCode('        seq = []')
PrintHelper.PrintCode('        while nr2 <= self.maxnum:')
PrintHelper.PrintCode('            nr3 = nr1 + nr2')
PrintHelper.PrintCode('            nr1 = nr2')
PrintHelper.PrintCode('            nr2 = nr3')
PrintHelper.PrintCode('            seq.append( nr1 )')
PrintHelper.PrintCode('        return FiboIterable( seq )')
PrintHelper.PrintCode('fseq = Fibo()')
PrintHelper.PrintCode('for n in fseq:')
PrintHelper.PrintCode('    print( n, end=\" \" )')
class FiboIterable:
    def __init__( self, seq ):
        self.seq = seq
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
class Fibo:
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
    def __iter__( self ):
        nr1 = 0
        nr2 = 1
        seq = []
        while nr2 <= self.maxnum:
            nr3 = nr1 + nr2
            nr1 = nr2
            nr2 = nr3
            seq.append( nr1 )
        return FiboIterable( seq )
fseq = Fibo()
for n in fseq:
    print( n, end=" " )
PrintHelper.PrintSubtitle('函数集合')
PrintHelper.PrintSampleWithDescription('zip(@lists)','同质化组织迭代zip([1,2,3],[4,5,6],[7,8,9])=>([1,4,7],[2,5,8],[3,6,9])')
PrintHelper.PrintSampleWithDescription('reversed(@list)','倒序')
PrintHelper.PrintSampleWithDescription('sorted(@list[,reverse=@bool])','排序')
PrintHelper.PrintHint('zip(),zip()函数可用以将多种迭代方式的数据组织在一起',"for...in...遍历时以最短的长度为准")
PrintHelper.PrintCode('seq=zip(\"I am a string\",[1,2,3],(1,\"q\",3))')
PrintHelper.PrintCode('for x in seq:')
PrintHelper.PrintCode('    print(x)')
seq=zip("I am a string",[1,2,3],(1,"q",3))
for x in seq:
    print(x)
PrintHelper.PrintTitle('Generators')
print('一些标准的方法就是Generator,诸如range()')
print('Generator的实现基于yield关键字')
print('当调用__next__()方法时,方法执行直到yield关键字')
PrintHelper.PrintCode('def fibonacci(maxnum):')
PrintHelper.PrintCode('    nr1=0')
PrintHelper.PrintCode('    nr2=1')
PrintHelper.PrintCode('    while nr2<maxnum:')
PrintHelper.PrintCode('        nr3=nr1+nr2')
PrintHelper.PrintCode('        nr1=nr2')
PrintHelper.PrintCode('        nr2=nr3')
PrintHelper.PrintCode('        yield nr1')
PrintHelper.PrintCode('fseq=fibonacci(1000)')
def fibonacci(maxnum):
    nr1=0
    nr2=1
    while nr2<maxnum:
        nr3=nr1+nr2
        nr1=nr2
        nr2=nr3
        yield nr1
fseq=fibonacci(1000)
PrintHelper.PrintCode('for n in fseq:')
PrintHelper.PrintCode('    print(n,end=\",\")')
PrintHelper.PrintCode('print()')
for n in fseq:
    print(n,end=",")
print()
PrintHelper.PrintSubtitle('yield近似与pop(),数据只能被一次使用'
                          ,"使用了yield关键词后,对象会被自动生成,包含了__next__()和__iter__()的实现")
PrintHelper.PrintCode('for n in fseq:')
PrintHelper.PrintCode('    print(n,end=\",\")')
for n in fseq:
    print(n,end=",")
PrintHelper.PrintSubtitle('Generator Expressions,生成器表达式')
print('由于list可以被转变为一个interator,由此又可以转变为一个generator')
print('python引进了一个与generator相似的概念,称作generator expression')
print('这种语法就像列表推导式一样,除了方括号用圆括号替代')
PrintHelper.PrintCode('seq=(x*x for x in range(11))')
PrintHelper.PrintCode('for x in seq:')
PrintHelper.PrintCode('    print(x,end=\",\")')
seq=(x*x for x in range(11))
for x in seq:
    print(x,end=",")
PrintHelper.PrintTitle('itertools Module')
PrintHelper.PrintHint('itertools,一个模块用以iterators的操作')
PrintHelper.PrintSubtitle('方法集合')
PrintHelper.PrintSampleWithDescription('chain(@iterable[,@iterable])','允许像迭代一个对象一样迭代多个iterable的集合')
PrintHelper.PrintSampleWithDescription('zip_longest()','与zip()方法相似,但是它创建了一个迭代器,它以其中最长的数据长度为准,而zip()以最短的为准')
PrintHelper.PrintSampleWithDescription('product(@iterable[,@iterable])','乘积,笛卡尔积')
PrintHelper.PrintSampleWithDescription('permutations(@iterable[,@length])','置换组合(均匀排列组合),考虑排列,指定个数对可迭代的数据作排列组合.Anm Cnm')
PrintHelper.PrintSampleWithDescription('combinations(@iterable[,@length])','组合,忽视排列')
PrintHelper.PrintSampleWithDescription('combinations_with_replacement(@iterable[,@length])','组合,非均匀排列组合')
PrintHelper.PrintHint('chain(@iterable[,@iterable])','允许像迭代一个对象一样迭代多个iterable的集合')
PrintHelper.PrintCode('import itertools')
PrintHelper.PrintCode('seq = itertools.chain( [1,2,3], [11,12,13,14], [x*x for x in range(1,6)] )')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item, end=\" \")')
import itertools
seq = itertools.chain( [1,2,3], [11,12,13,14], [x*x for x in range(1,6)] )
for item in seq:
    print( item, end=" ")
PrintHelper.PrintHint('zip_longest()','与zip()方法相似,但是它创建了一个迭代器,它以其中最长的数据长度为准,而zip()以最短的为准')
PrintHelper.PrintCode('seq = itertools.zip_longest( \"apple\", \"strawberry\", \"banana\", fillvalue=\" \")')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item )')
seq = itertools.zip_longest( "apple", "strawberry", "banana", fillvalue=" ")
for item in seq:
    print( item )
PrintHelper.PrintHint('product()','product(),乘积')
PrintHelper.PrintCode('seq = itertools.product( [1,2,3], \"ABC\", [\"apple\",\"banana\"] )')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item )')
seq = itertools.product( [1,2,3], "ABC", ["apple","banana"] )
for item in seq:
    print( item )
PrintHelper.PrintHint('permutations(@iterable[,@count])','排列,指定个数对可迭代的数据作排列组合.Anm Cnm')
PrintHelper.PrintCode('seq = itertools.permutations( [1,2,3], 2 )')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item )')
seq = itertools.permutations( [1,2,3], 2 )
for item in seq:
    print( item )
PrintHelper.PrintHint('combinations(@iterable[,@length])','组合,忽视排列')
PrintHelper.PrintCode('seq = itertools.combinations( [1,2,3], 2 )')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item )')
seq = itertools.combinations( [1,2,3], 2 )
for item in seq:
    print( item )
PrintHelper.PrintHint('combinations_with_replacement(@iterable[,@length])'
                      ,'组合,非均匀排列组合,跟permutation结果相似,但是其为不均匀组合')
PrintHelper.PrintCode('seq = itertools.combinations_with_replacement( [1,2,3], 2 )')
PrintHelper.PrintCode('for item in seq:')
PrintHelper.PrintCode('    print( item )')
seq = itertools.combinations_with_replacement( [1,2,3], 2 )
for item in seq:
    print( item )
