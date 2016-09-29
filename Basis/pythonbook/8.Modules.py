import PrintHelper
PrintHelper.PrintTitle('Modules')
print('如何引用一个模块')
print('i.e., 它的文件夹路径称为@path')
print('将引用模块的路径写入一个以.pth结尾的文件')
print('将其保存于以下目录"\Python\Lib\site-packages"')
print('默认的引用目录在模块sys下')
print('可以通过输出sys.path指令进行查看(需要先引用)')
PrintHelper.PrintCode('import sys')
import sys
PrintHelper.PrintCode('print(sys.path)')
print(sys.path)
