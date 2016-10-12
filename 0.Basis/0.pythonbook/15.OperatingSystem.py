import PrintHelper
import os
PrintHelper.PrintTitle('Basics of Operating System,操作系统基础')
print('电脑由硬件组成,软件由程序组成')
print('软件使用了硬件提供的基础设施')
print('在早期的编程中,程序员直接操控硬件')
print('现在的硬件变得极其复杂和多样化,直接操控硬件通常不是可行的方案')
print('所以现在程序通常通过操作系统来来间接地操控硬件.')
print('操作系统被认为是介于程序和硬件之间的一层,用以提供程序操作硬件的高级方法.')
print('像Microsoft的Windows,Apple的MacOS,open-source的Linux等等')
print('它们都提供操作硬件的高级方法.但是同样的它们之间的方法并不尽相同,名称或者参数.')
print('如果你用Python写直接操控硬件的程序的话,那么这种程序并不能跨系统兼容的.')
print('而os模块提供了用以无视操作系统来操作硬件的方法')
print('从根本上说os模块对于不同的操作系统有着不同的实现,但你和你的程序可以不知道它的细节.')
print('这并不代表你可以无视操作系统的错综复杂的东西.')
print('举例来说:在Windows下,你需要提供驱动器号来访问文件,而在MacOS下并不支持这种形式的访问.')
print('另一个例子是:安全和文件访问权限在Linux下更为灵活,所以它将报出比其它操作系统更多类型的错误和警告.')
print('总而言之,os模块是一种不错的对于操作系统之间差异的妥协方案.')
PrintHelper.PrintTitle('Command Prompt,命令指示符')
print('所有你对操作系统的操作都可以以命令指示符的形式反映于操作系统上')
print('大多数linux用户对命令指示符比较熟悉,对于图形界面的用户可能没有意识到这一点.')
print('python的程序可以在命令执行工具中以这种方式启动 python <programName>.py')
PrintHelper.PrintTitle('File System')
print('文件系统是一种按照树形结构组织的文件夹或文件')
print('通常有一个根目录,称为root,作为所有其他内容的访问入口.')
print('根据操作系统的不同,它被用/或者\\来表示.')
print('MacOS和linux使用forward slash(/),而在window上使用back slash(\\)表示')
print('笔者建议使用/,因为\\在很多情况下被用作特殊的转义符号')
PrintHelper.PrintTitle('os functions')
PrintHelper.PrintHint('getcwd()')
PrintHelper.PrintCode('print(os.getcwd())')
print(os.getcwd())
PrintHelper.PrintHint('chdir(@path)')
PrintHelper.PrintCode('home=os.getcwd()')
home=os.getcwd()
PrintHelper.PrintCode('print(os.getcwd())')
print(os.getcwd())
PrintHelper.PrintCode('os.chdir(\"..\")')
os.chdir("..")
PrintHelper.PrintCode('print(os.getcwd())')
print(os.getcwd())
PrintHelper.PrintCode('os.chdir(home)')
os.chdir(home)
PrintHelper.PrintCode('print(os.getcwd())')
print(os.getcwd())
PrintHelper.PrintHint('listdir()')
PrintHelper.PrintCode('print(os.listdir())')
print(os.listdir())
PrintHelper.PrintHint('system(@cmd) ')
PrintHelper.PrintCode('print(\'os.system(\"cmd\")\')')
print('os.system("cmd")')
print('以上指令将打开cmd窗口')