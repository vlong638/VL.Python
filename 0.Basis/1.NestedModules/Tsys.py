import PrintHelper
import sys
PrintHelper.PrintSubtitle('Encoding,编码')
print(sys.getfilesystemencoding())
PrintHelper.PrintHint('sys.getdefaultencoding()')
PrintHelper.PrintCode('print(sys.getdefaultencoding())')
print(sys.getdefaultencoding())
PrintHelper.PrintHint('sys.getfilesystemencoding()')
PrintHelper.PrintCode('print(sys.getfilesystemencoding())')
print(sys.getfilesystemencoding())
PrintHelper.PrintSubtitle('输出对应当前encoding的字符集')
PrintHelper.PrintCode('for i in range(16):')
PrintHelper.PrintCode('    if i < 10:')
PrintHelper.PrintCode('        print( \' \'+chr( ord( \'0\' )+i ), end= \' \' )')
PrintHelper.PrintCode('    else:')
PrintHelper.PrintCode('        print( \' \'+chr( ord( \'A\' )+i-10 ), end= \' \' )')
PrintHelper.PrintCode('print()')
PrintHelper.PrintCode('for i in range( 10, 16 ):')
PrintHelper.PrintCode('    print( chr( ord( \'A\' )+i-10 ), end= \' \' )')
PrintHelper.PrintCode('    for j in range( 16 ):')
PrintHelper.PrintCode('         c = i*16+j')
PrintHelper.PrintCode('         print( \' \'+chr( c ), end= \' \' )')
PrintHelper.PrintCode('    print()')
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end= ' ' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end= ' ' )
print()
for i in range( 10, 16 ):
    print( chr( ord( 'A' )+i-10 ), end= ' ' )
    for j in range( 16 ):
         c = i*16+j
         print( ' '+chr( c ), end= ' ' )
    print()
PrintHelper.PrintSubtitle('The Command Line,命令行')
PrintHelper.PrintHint('sys.argv,用以接收命令行参数')
print('你可以使用sys.argv来接收命令行参数,示例如下')
print('import sys')
print('# 3 variables for holding the command line parameters')
print('inputfile = \"input.txt\"')
print('outputfile = \"output.txt\"')
print('shift = 3')
print('# Processing the command line parameters')
print('# (works with 0, 1, 2, or 3 parameters)')
print('if len( sys.argv ) > 1:')
print('    inputfile = sys.argv[1]')
print('if len( sys.argv ) > 2:')
print('    outputfile = sys.argv[2]')
print('if len( sys.argv ) > 3:')
print('    try:')
print('        shift = int( sys.argv[3] )')
print('    except TypeError:')
print('        print( sys.argv[3], \"is not an integer.\" )')
print('        sys.exit(1)')
PrintHelper.PrintHint('sys.exit([@ResultCode])')
print('可以返回一个指定的参数,通常用作异常编码')
