import PrintHelper
PrintHelper.PrintTitle('datetime模块')
PrintHelper.PrintHint('@datetime=datetime.now()')
PrintHelper.PrintHint('@datetime=datetime.datetime(@year,@month,@day,@hour,@minute,@second)')
PrintHelper.PrintHint('@year=@datetime.year')
PrintHelper.PrintHint('@month=@datetime.month')
PrintHelper.PrintHint('@day=@datetime.day')
PrintHelper.PrintHint('@hour=@datetime.hour')
PrintHelper.PrintHint('@minute=@datetime.minute')
PrintHelper.PrintHint('@second=@datetime.second')
PrintHelper.PrintHint('@microsecond=@datetime.microsecond')

PrintHelper.PrintTitle('collections模块')
print('collection模块提供了一些集合数据的特殊处理,诸如出现频次统计.')
PrintHelper.PrintHint('@counter=collections.Counter(@data),建立计数器')
PrintHelper.PrintCode('from collections import Counter')
PrintHelper.PrintCode('data = [ \"apple\", \"banana\", \"apple\", \"banana\", \"apple\", \"cherry\" ]')
PrintHelper.PrintCode('c = Counter( data )')
PrintHelper.PrintCode('print( c )')
from collections import Counter
data = [ "apple", "banana", "apple", "banana", "apple", "cherry" ]
c = Counter( data )
print( c )
PrintHelper.PrintHint('@counter.most_common(@index),获取对应计数排名的数据项')
PrintHelper.PrintCode('print( c.most_common( 1 ) )')
print( c.most_common( 1 ) )
PrintHelper.PrintHint('@counter.update(@data),导入新数据')
PrintHelper.PrintCode('data2 = [ \"orange\", \"cherry\", \"cherry\", \"cherry\", \"cherry\" ]')
PrintHelper.PrintCode('c.update( data2 )')
PrintHelper.PrintCode('print( c )')
PrintHelper.PrintCode('print( c.most_common() )')
data2 = [ "orange", "cherry", "cherry", "cherry", "cherry" ]
c.update( data2 )
print( c )
print( c.most_common() )

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

PrintHelper.PrintTitle('glob模块')
print('glob模块用于创建使用通配符匹配后的文件列表')
PrintHelper.PrintHint('?','指示任意字符')
PrintHelper.PrintHint('*','指示任意序列的字符集合')
PrintHelper.PrintHint('[@characters]','匹配[]内的所有字符集合')
PrintHelper.PrintSubtitle('示例')
PrintHelper.PrintCode('from glob import glob')
PrintHelper.PrintCode('glist = glob( \"*.?y\" )')
PrintHelper.PrintCode('for name in glist:')
PrintHelper.PrintCode('    print( name )')
from glob import glob
glist = glob( "*.?y" )
for name in glist:
    print( name )

PrintHelper.PrintTitle('statistics模块用以访问复杂的统计方法','StatisticsError通用的异常')
print('所有的方法都以列表数据或者迭代器为数据')
PrintHelper.PrintCode('from statistics import mean, median, mode, stdev, variance, StatisticsError')
PrintHelper.PrintCode('data = [ 4, 5, 1, 1, 2, 2, 2, 2, 3, 3, 3 ]')
from statistics import mean, median, mode, stdev, variance, StatisticsError
data = [ 4, 5, 1, 1, 2, 2, 2, 2, 3, 3, 3 ]
PrintHelper.PrintHint('statistics.mean(),求平均数,全部和除以个数')
PrintHelper.PrintCode('print( \"mean:\", mean( data ) )')
print( "mean:", mean( data ) )
PrintHelper.PrintHint('statistics.median(),取中位数,如上限5则为2.5')
PrintHelper.PrintCode('print( \"median:\", median( data ) )')
print( "median:", median( data ) )
PrintHelper.PrintHint('statistics.mode(),众数,出现次数最多的数')
PrintHelper.PrintCode('print( \"mode:\", mode( data ) )')
print( "mode:", mode( data ) )
print()
print('众数方法只能返回唯一的众数,当出现多个众数时返回异常')
PrintHelper.PrintCode('data = [ 4, 5, 1, 1, 2, 2, 2, 3, 3, 3 ]')
PrintHelper.PrintCode('try:')
PrintHelper.PrintCode('    print( \"mode:\", mode( data ) )')
PrintHelper.PrintCode('except StatisticsError as e:')
PrintHelper.PrintCode('    print( e )')
data = [ 4, 5, 1, 1, 2, 2, 2, 3, 3, 3 ]
try:
    print( "mode:", mode( data ) )
except StatisticsError as e:
    print( e )
PrintHelper.PrintHint('statistics.stdev(),标准差,方差的算数平方根')
PrintHelper.PrintCode('print( \"st.dev.: {:.3f}\".format( stdev( data ) ) )')
print( "st.dev.: {:.3f}".format( stdev( data ) ) )
PrintHelper.PrintHint('statistics.variance(),方差,各数距离平均数的平方合除以个数')
PrintHelper.PrintCode('print( \"variance: {:.3f}\".format( variance( data ) ) )')
print( "variance: {:.3f}".format( variance( data ) ) )

