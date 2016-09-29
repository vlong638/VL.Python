import PrintHelper
PrintHelper.PrintTitle('urllib模块')
print('urllib模块让你可以像访问文件一样访问网页')
PrintHelper.PrintHint('@webPage=urllib.request.urlopen(@url)','urllib.HTTPError','urllib.URLError')
PrintHelper.PrintCode('from urllib.request import urlopen')
PrintHelper.PrintCode('from urllib.error import HTTPError, URLError')
PrintHelper.PrintCode('from sys import exit')
PrintHelper.PrintCode('try:')
PrintHelper.PrintCode('    u = urlopen( \"http://www.python.org\" )')
PrintHelper.PrintCode('except HTTPError as e:')
PrintHelper.PrintCode('    print( \"HTTP Error\", e )')
PrintHelper.PrintCode('    sys.exit()')
PrintHelper.PrintCode('except URLError as e:')
PrintHelper.PrintCode('    print( \"URL error\", e )')
PrintHelper.PrintCode('    sys.exit()')
PrintHelper.PrintCode('    ')
PrintHelper.PrintCode('for i in range( 5 ):')
PrintHelper.PrintCode('    text = u.readline()')
PrintHelper.PrintCode('    print( text )')
PrintHelper.PrintCode('u.close()')
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import exit
try:
    u = urlopen( "http://www.python.org" )
except HTTPError as e:
    print( "HTTP Error", e )
    sys.exit()
except URLError as e:
    print( "URL error", e )
    sys.exit()
    
for i in range( 5 ):
    text = u.readline()
    print( text )
u.close()
