import PrintHelper
import os
PrintHelper.PrintTitle('os functions')
PrintHelper.PrintSubtitle('getcwd()')
PrintHelper.PrintCode('print(os.getcwd())')
print(os.getcwd())
PrintHelper.PrintSubtitle('listdir()')
PrintHelper.PrintCode('print(os.listdir())')
print(os.listdir())
PrintHelper.PrintSubtitle('chdir()')
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
PrintHelper.PrintSubtitle('system(),可用以执行系统指令')
PrintHelper.PrintCode('print(os.system(cmd))')
print('以上指令将打开cmd窗口')
PrintHelper.PrintSubtitle('os.path methods')
PrintHelper.PrintSubtitle('Prepares')
PrintHelper.PrintCode('os.chdir(\"..\\FilesForTest\")')
PrintHelper.PrintCode('print(os.getcwd())')
os.chdir("..\FilesForTest")
print(os.getcwd())
PrintHelper.PrintCode('filePath="a.txt"')
filePath="a.txt"
print(filePath)
PrintHelper.PrintCode('print(filePath)')
PrintHelper.PrintCode('with open(filePath,"a") as fp:')
PrintHelper.PrintCode('    fp.close()')
with open(filePath,"a") as fp:
    fp.close()
PrintHelper.PrintHint('os.path.exists(@path)')
PrintHelper.PrintCode('print(os.path.exists(filePath))')
PrintHelper.PrintCode('print(os.path.exists(filePath))')
print(os.path.exists(filePath))
PrintHelper.PrintHint('os.path.isfile(@path)')
PrintHelper.PrintCode('print(os.path.isfile(filePath))')
PrintHelper.PrintCode('print(os.path.isfile(filePath))')
print(os.path.isfile(filePath))
PrintHelper.PrintHint('os.path.isdir(@path)')
PrintHelper.PrintCode('print(os.path.isdir(filePath))')
PrintHelper.PrintCode('print(os.path.isdir(filePath))')
print(os.path.isdir(filePath))
PrintHelper.PrintHint('os.path.join(@partialPath1[,@partialPathN])')
PrintHelper.PrintCode('print(os.path.join(os.getcwd(),filePath))')
print(os.path.join(os.getcwd(),filePath))
PrintHelper.PrintHint('os.path.basename(@path)')
PrintHelper.PrintCode('print(os.path.basename("C:\Windows\win.ini"))')
print(os.path.basename("C:\Windows\win.ini"))
PrintHelper.PrintHint('os.path.dirname(@path)')
PrintHelper.PrintCode('print(os.path.dirname(C:\Windows\win.ini))')
print(os.path.dirname("C:\Windows\win.ini"))
PrintHelper.PrintHint('os.path.getsize(@path)')
PrintHelper.PrintCode('print(os.path.getsize(filePath))')
print(os.path.getsize(filePath))
