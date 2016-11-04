#更多详情参考http://www.jb51.net/article/48771.htm
#counter=collections.Counter(@data)
import PrintHelper
PrintHelper.PrintTitle('collections模块')
PrintHelper.PrintTitle('1.Counter')
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
PrintHelper.PrintTitle('2.deque,double-end-queue,')
PrintHelper.PrintHint('双端队列 其实现了两个特殊的方法 .popleft() appendleft()')
print('原生的list也可以从头部添加和取出对象')
print('l.insert(0,v)')
print('l.pop(0)')
print('但是值得注意的是,list对象的这两种用法的时间复杂度是O(n),也就是随着元素数量的增加耗时')
print('而deque对象则是O(1)的复杂度,所以有双端队列的需求时,记得要用deque')
print('deque提供了其他的好用方法,比如@deque.rotate(@index),可以用于制造无限循环的跑马灯')
PrintHelper.PrintCode('import sys')
PrintHelper.PrintCode('import time')
PrintHelper.PrintCode('from collections import deque')
PrintHelper.PrintCode('fancy_loading = deque(\'>--------------------\')')
PrintHelper.PrintCode('index=0')
PrintHelper.PrintCode('while True:')
PrintHelper.PrintCode('    print \'\\r%s\' % \'\'.join(fancy_loading),')
PrintHelper.PrintCode('    fancy_loading.rotate(1)')
PrintHelper.PrintCode('    sys.stdout.flush()')
PrintHelper.PrintCode('    time.sleep(0.08)')
PrintHelper.PrintCode('    index+=1')
PrintHelper.PrintCode('    if index>10:')
PrintHelper.PrintCode('        break')
import sys
import time
from collections import deque
fancy_loading = deque('>--------------------')
index=0
while True:
    print('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
    index+=1
    if index>10:
        break
PrintHelper.PrintTitle('3.namedtuple()')
PrintHelper.PrintHint('tuple并不支持使用名称访问数据,使用namedtuple可以改进数据可读性')
PrintHelper.PrintCode('from collections import namedtuple')
PrintHelper.PrintCode('websites = [')
PrintHelper.PrintCode('    (\'Sohu\', \'http://www.google.com/\', u\'张朝阳\'),')
PrintHelper.PrintCode('    (\'Sina\', \'http://www.sina.com.cn/\', u\'王志东\'),')
PrintHelper.PrintCode('    (\'163\', \'http://www.163.com/\', u\'丁磊\')')
PrintHelper.PrintCode(']')
PrintHelper.PrintCode('Website = namedtuple(\'Website\', [\'name\', \'url\', \'founder\'])')
PrintHelper.PrintCode('for website in websites:')
PrintHelper.PrintCode('    website = Website._make(website)')
PrintHelper.PrintCode('    print website')
PrintHelper.PrintCode('# Result:')
PrintHelper.PrintCode('Website(name=\'Sohu\', url=\'http://www.google.com/\', founder=u\'\\u5f20\\u671d\\u9633\')')
PrintHelper.PrintCode('Website(name=\'Sina\', url=\'http://www.sina.com.cn/\', founder=u\'\\u738b\\u5fd7\\u4e1c\')')
PrintHelper.PrintCode('Website(name=\'163\', url=\'http://www.163.com/\', founder=u\'\\u4e01\\u78ca\')')
from collections import namedtuple
websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website)
    print(website)
# Result:
Website(name='Sohu', url='http://www.google.com/', founder=u'\u5f20\u671d\u9633')
Website(name='Sina', url='http://www.sina.com.cn/', founder=u'\u738b\u5fd7\u4e1c')
Website(name='163', url='http://www.163.com/', founder=u'\u4e01\u78ca')
PrintHelper.PrintTitle('4.OrderedDict')
PrintHelper.PrintHint('有序dict dict这个数据结构由于hash的特性是无序的 tips:可以用 for k,v in @dict.items()访问')
PrintHelper.PrintCode('from collections import OrderedDict')
PrintHelper.PrintCode('items = (')
PrintHelper.PrintCode('    (\'A\', 1),')
PrintHelper.PrintCode('    (\'B\', 2),')
PrintHelper.PrintCode('    (\'C\', 3)')
PrintHelper.PrintCode(')')
PrintHelper.PrintCode('regular_dict = dict(items)')
PrintHelper.PrintCode('ordered_dict = OrderedDict(items)')
PrintHelper.PrintCode('print \'Regular Dict:\'')
PrintHelper.PrintCode('for k, v in regular_dict.items():')
PrintHelper.PrintCode('    print k, v')
PrintHelper.PrintCode('print \'Ordered Dict:\'')
PrintHelper.PrintCode('for k, v in ordered_dict.items():')
PrintHelper.PrintCode('    print k, v')
from collections import OrderedDict
items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)
regular_dict = dict(items)
ordered_dict = OrderedDict(items)
print('Regular Dict:')
for k, v in regular_dict.items():
    print(k, v)
print('Ordered Dict:')
for k, v in ordered_dict.items():
    print(k, v)
PrintHelper.PrintTitle('5.defaultdict')
PrintHelper.PrintHint(',带默认值的dict 针对原版的dict增加了默认值初始化功能,原版的dict访问不存在的key时报错')
PrintHelper.PrintCode('from collections import defaultdict')
PrintHelper.PrintCode('members = [')
PrintHelper.PrintCode('    # Sex, name')
PrintHelper.PrintCode('    [\'male\', \'John\'],')
PrintHelper.PrintCode('    [\'male\', \'Jack\'],')
PrintHelper.PrintCode('    [\'female\', \'Lily\'],')
PrintHelper.PrintCode('    [\'male\', \'Pony\'],')
PrintHelper.PrintCode('    [\'female\', \'Lucy\'],')
PrintHelper.PrintCode(']')
PrintHelper.PrintCode('result = defaultdict(list)')
PrintHelper.PrintCode('for sex, name in members:')
PrintHelper.PrintCode('    result[sex].append(name)')
PrintHelper.PrintCode('print result')
from collections import defaultdict
members = [
    # Sex, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)
print(result)
