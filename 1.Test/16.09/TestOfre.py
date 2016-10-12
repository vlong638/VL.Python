import PrintHelper
import re
PrintHelper.PrintHint('re.compile()')
PrintHelper.PrintCode('pattern=re.compile(r\"hello\")')
pattern=re.compile(r"hello")
PrintHelper.PrintHint('@pattern.match()')
PrintHelper.PrintCode('match=pattern.match(\"hello,hello,hello world!\")')
match=pattern.match("hello,hello,hello world!")
PrintHelper.PrintHint('@match.group()')
PrintHelper.PrintCode('if match:')
PrintHelper.PrintCode('    print(match.group())')
if match:
    print(match.group())
PrintHelper.PrintCode('if match:')
PrintHelper.PrintCode('    for group in match.groups():')
PrintHelper.PrintCode('        print(group)')
if match:
    print(type(match.groups()))
    print(match.groups())
PrintHelper.PrintSubtitle('检测中文个数')
PrintHelper.PrintCode('count=0')
PrintHelper.PrintCode('for letter in \"我是中文121212i am english,我不是中文\":')
PrintHelper.PrintCode('    if re.match(\'([\\u4e00-\\u9fa5])+\',letter):')
PrintHelper.PrintCode('        count+=1')
PrintHelper.PrintCode('print(count)')
count=0
for letter in "我是中文121212i am english,我不是中文":
    if re.match('([\u4e00-\u9fa5])+',letter):
        count+=1
print(count)
