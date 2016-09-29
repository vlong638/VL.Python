import PrintHelper
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
