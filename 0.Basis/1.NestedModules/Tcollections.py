import PrintHelper
PrintHelper.PrintTitle('collections模块')
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
