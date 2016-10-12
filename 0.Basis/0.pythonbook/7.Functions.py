#标题
titlePattern=":-^80"
#子标题
subTitlePattern=":-^40"
#特别信息
tipsTitlePattern=":*^40"

print(("{"+titlePattern+"}").format("Functions"))
print("def <function_name>(<parameter_list>):")
print("    <statements")
print(("{"+titlePattern+"}").format("simple function,no parameter,no return"))
def helloWorld():
    print('Hello,world!')
print("def helloWorld():")
print("    print('Hello,world!')")
print("HelloWorld()")
print("=>")
helloWorld()
print(("{"+titlePattern+"}").format("function with parameter,no return"))
def printTypeName(anyValue):
    if isinstance(anyValue,int):
        print("int")
    elif isinstance(anyValue,float):
        print("float")
    elif isinstance(anyValue,str):
        print("str")
    else:
        print("other")
print('def printTypeName(anyValue):')
print('    if isinstance(anyValue,int):')
print('        print("int")')
print('    elif isinstance(anyValue,float):')
print('        print("float")')
print('    elif isinstance(anyValue,str):')
print('        print("str")')
print('    else:')
print('        print("other")')
print("printTypeName(1)=>")
printTypeName(1)
print("printTypeName(1.0)=>")
printTypeName(1.0)
print("printTypeName('1')=>")
printTypeName('1')
print(("{"+titlePattern+"}").format("function with parameter and single return"))
def getTypeName(anyValue):
    if isinstance(anyValue,int):
        return "int"
    elif isinstance(anyValue,float):
        return "float"
    elif isinstance(anyValue,str):
        return "str"
    else:
        return "other"
print('def getTypeName(anyValue):')
print('    if isinstance(anyValue,int):')
print('        return "int"')
print('    elif isinstance(anyValue,float):')
print('        return "float"')
print('    elif isinstance(anyValue,str):')
print('        return "str"')
print('    else:')
print('        return "other"')
print('print(GetTypeName(1))=>')
print(getTypeName(1))
print('print(getTypeName(1.0))=>')
print(getTypeName(1.0))
print('print(getTypeName("1"))=>')
print(getTypeName("1"))
print(("{"+titlePattern+"}").format("function with parameter and multiple return"))
def getTypeNameAndLength(anyValue):
    if isinstance(anyValue,int):
        valueType="int"
    elif isinstance(anyValue,float):
        valueType="float"
    elif isinstance(anyValue,str):
        valueType="str"
    else:
        valueType="other"
    return valueType,len(str(anyValue))
print('def getTypeNameAndLength(anyValue):')
print('    if isinstance(anyValue,int):')
print('        valueType="int"')
print('    elif isinstance(anyValue,float):')
print('        valueType="float"')
print('    elif isinstance(anyValue,str):')
print('        valueType="str"')
print('    else:')
print('        valueType="other"')
print('    return valueType,len(anyValue)')
print('value,length=GetTypeNameAndLength(1)')
print('print(value,length)')
value,length=getTypeNameAndLength(1)
print("=>",value,length)
print('value,length=GetTypeNameAndLength(1.0)')
print('print(value,length)')
value,length=getTypeNameAndLength(1.0)
print("=>",value,length)
print('value,length=GetTypeNameAndLength("1")')
print('print(value,length)')
value,length=getTypeNameAndLength("1")
print("=>",value,)
print(("{"+titlePattern+"}").format("test of indefinite parameter"))
def test3(*args,**kargs):
    print(type(args))
    print(args)
    print(type(kargs))
    print(kargs)
print('def test3(*args,**kargs):')
print('    print(type(args))')
print('    print(args)')
print('    print(type(kargs))')
print('    print(kargs)')
print(('{'+subTitlePattern+'}').format('test3(1,2)'))
test3(1,2)
print(('{'+subTitlePattern+'}').format('test3(1,b=2)'))
test3(1,b=2)
print(('{'+subTitlePattern+'}').format('test3(1,2,b=2,c=3)'))
test3(1,2,b=2,c=3)
import PrintHelper
PrintHelper.PrintTitle("Anonymous Functions")
func1=lambda value1,value2:value1*value2
print('@functionName=lambda @inputvalue:@outputValue')
print('func1=lambda value1,value2:value1*value2')
PrintHelper.PrintSubtitle('print(func1(2,5))')
print(func1(2,5))



