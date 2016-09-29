import PrintHelper
PrintHelper.PrintTitle('Basic Of Sets')
print('Sets是无序的数据结构,它只能存储unique的元素,它使用{}来创建')
print('不能通过set[index]或者set[key]的形式进行访问')
print('只能通过for循环或者in操作符来检测数据项')
print('set使用dictionary得以实现,特殊的地方在于,它把dictionary的key用作元素')
PrintHelper.PrintSubtitle('创建Set')
PrintHelper.PrintCode('fruitSet={\"apple\",\"banana\",\"cherry\"}')
fruitSet={"apple","banana","cherry"}
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('helloSet=set([\"hello\",\"welcome\"])')
helloSet=set(["hello","welcome"])
PrintHelper.PrintCode('print(helloSet)')
print(helloSet)
PrintHelper.PrintTitle('Set Methods')
PrintHelper.PrintSubtitle('add(),单个增加')
PrintHelper.PrintCode('fruitSet={\"apple\",\"banana\",\"cherry\"}')
fruitSet={"apple","banana","cherry"}
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('fruitSet.add(\"apple\")')
fruitSet.add("apple")
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintSubtitle('update(),批量增加')
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('fruitSet.update(\"orange\")')
fruitSet.update("orange")
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('fruitSet.update([\"orange\",\"watermelon\"])')
fruitSet.update(["orange","watermelon"])
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintSubtitle('remove()')
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('fruitSet.remove(\"orange\")')
fruitSet.remove("orange")
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintSubtitle('discard(),和remove的区别是不存在元素时不报错')
PrintHelper.PrintCode('print(fruitSet)')
PrintHelper.PrintCode('fruitSet.discard(\"orange\")')
PrintHelper.PrintCode('for letter in \"orange\":')
PrintHelper.PrintCode('    fruitSet.discard(letter)')
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
fruitSet.discard("orange")
for letter in "orange":
    fruitSet.discard(letter)
print(fruitSet)
PrintHelper.PrintSubtitle('clear()')
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintCode('fruitSet.clear()')
fruitSet.clear()
PrintHelper.PrintCode('print(fruitSet)')
print(fruitSet)
PrintHelper.PrintSubtitle('pop(),pop()是无序的推送一个数据出来的.')
PrintHelper.PrintCode('while len(fruitSet)>0:')
PrintHelper.PrintCode('    print(fruitSet.pop())')
while len(fruitSet)>0:
    print(fruitSet.pop())
PrintHelper.PrintSubtitle('copy(),拷贝')
PrintHelper.PrintCode('fruitSet={\"apple\",\"banana\",\"cherry\"}')
PrintHelper.PrintCode('print(fruitSet)')
PrintHelper.PrintCode('fruitSetCopy=fruitSet.copy()')
PrintHelper.PrintCode('print(fruitSetCopy)')
fruitSet={"apple","banana","cherry"}
print(fruitSet)
fruitSetCopy=fruitSet.copy()
print(fruitSetCopy)
PrintHelper.PrintSubtitle('union(),并集')
PrintHelper.PrintCode('fruitSet1={\"apple\",\"cherry\"}')
PrintHelper.PrintCode('print(fruitSet1)')
PrintHelper.PrintCode('fruitSet2={\"banana\",\"cherry\"}')
PrintHelper.PrintCode('print(fruitSet2)')
PrintHelper.PrintCode('fruitSetUnion=fruitSet1.union(fruitSet2)')
PrintHelper.PrintCode('print(fruitSetUnion)')
fruitSet1={"apple","cherry"}
print(fruitSet1)
fruitSet2={"banana","cherry"}
print(fruitSet2)
fruitSetUnion=fruitSet1.union(fruitSet2)
print(fruitSetUnion)
PrintHelper.PrintSubtitle('intersection(),交集')
PrintHelper.PrintCode('fruitIntersection=fruitSet1.intersection(fruitSet2)')
PrintHelper.PrintCode('print(fruitIntersection)')
fruitIntersection=fruitSet1.intersection(fruitSet2)
print(fruitIntersection)
PrintHelper.PrintSubtitle('difference(),差异')
PrintHelper.PrintCode('fruitDifference=fruitSet1.difference(fruitSet2)')
PrintHelper.PrintCode('print(fruitDifference)')
fruitDifference=fruitSet1.difference(fruitSet2)
print(fruitDifference)
PrintHelper.PrintSubtitle('参数定义')
PrintHelper.PrintCode('fruitSet1={\"apple\",\"cherry\"}')
PrintHelper.PrintCode('fruitSet2={\"cherry\"}')
PrintHelper.PrintCode('fruitSet3={\"orange\"}')
fruitSet1={"apple","cherry"}
PrintHelper.PrintCode('print(fruitSet1)')
print(fruitSet1)
fruitSet2={"cherry"}
PrintHelper.PrintCode('print(fruitSet2)')
print(fruitSet2)
fruitSet3={"orange"}
PrintHelper.PrintCode('print(fruitSet3)')
print(fruitSet3)
PrintHelper.PrintSubtitle('isdisjoint(),无交集')
PrintHelper.PrintCode('print(fruitSet1.disjoint(fruitSet2))')
print(fruitSet1.isdisjoint(fruitSet2))
PrintHelper.PrintCode('print(fruitSet1.disjoint(fruitSet3))')
print(fruitSet1.isdisjoint(fruitSet3))
PrintHelper.PrintSubtitle('issubset(),子集')
PrintHelper.PrintCode('print(fruitSet1.issubset(fruitSet2))')
print(fruitSet1.issubset(fruitSet2))
PrintHelper.PrintCode('print(fruitSet2.issubset(fruitSet1))')
print(fruitSet2.issubset(fruitSet1))
PrintHelper.PrintSubtitle('issuperset(),超集')
PrintHelper.PrintCode('print(fruitSet1.issuperset(fruitSet2))')
print(fruitSet1.issuperset(fruitSet2))
PrintHelper.PrintCode('print(fruitSet2.issuperset(fruitSet1))')
print(fruitSet2.issuperset(fruitSet1))
PrintHelper.PrintSubtitle('frozenset')
PrintHelper.PrintCode('frozenset1=frozenset([\"apple\",\"orange\"])')
frozenset1=frozenset(["apple","orange"])
PrintHelper.PrintCode('print(frozenset1)')
print(frozenset1)
PrintHelper.PrintCode('frozenset2=frozenset([\"banana\",\"cherry\",\"orange\"])')
frozenset2=frozenset(["banana","cherry","orange"])
PrintHelper.PrintCode('print(frozenset2)')
print(frozenset2)
PrintHelper.PrintCode('print(frozenset1.union(frozenset2))')
print(frozenset1.union(frozenset2))

