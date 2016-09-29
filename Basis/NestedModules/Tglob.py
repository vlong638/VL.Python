import PrintHelper
PrintHelper.PrintTitle('glob模块')
print('glob模块用于创建使用通配符匹配后的文件列表')
PrintHelper.PrintHint('?','指示任意字符')
PrintHelper.PrintHint('*','指示任意序列的字符集合')
PrintHelper.PrintHint('[@characters]','匹配[]内的所有字符集合')
PrintHelper.PrintSubtitle('示例')
PrintHelper.PrintCode('from glob import glob')
PrintHelper.PrintCode('glist = glob( \"*.py\" )')
PrintHelper.PrintCode('for name in glist:')
PrintHelper.PrintCode('    print( name )')
from glob import glob
glist = glob( "*.py" )
for name in glist:
    print( name )
