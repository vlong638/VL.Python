print('Hello World!')

def testParam1(*param):
    for letter in param:
        print(letter)

def testParam2(**param):
    print(type(param));
    
testParam1("string1","string2")
testParam2()

re="我是中文 123 i am english"
if re.match('[ \u4e00 -\u9fa5]+',x) = None:
    
