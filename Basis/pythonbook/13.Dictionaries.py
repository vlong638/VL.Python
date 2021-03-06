import PrintHelper
PrintHelper.PrintTitle('Basics Of Dictionaries')
PrintHelper.PrintSubtitle('Claim A Dictionary')
PrintHelper.PrintCode('fruitBasket={\"apple\":3,\"banana\":5,\"cherry\":50}')
fruitBasket={"apple":3,"banana":5,"cherry":50}
PrintHelper.PrintSubtitle('Access A Dictionary Value')
PrintHelper.PrintCode('print(fruitBasket[\"banana\"])')
print(fruitBasket["banana"])
PrintHelper.PrintSubtitle('Loop By for')
PrintHelper.PrintCode('for fruit in fruitBasket:')
PrintHelper.PrintCode('    print(fruit)')
for fruit in fruitBasket:
    print(fruit)
PrintHelper.PrintSubtitle('Add Item to Dictionary')
PrintHelper.PrintCode('fruitBasket={\"apple\":3,\"banana\":5,\"cherry\":50}')
fruitBasket={"apple":3,"banana":5,"cherry":50}
PrintHelper.PrintCode('print(fruitBasket)')
print(fruitBasket)
PrintHelper.PrintCode('fruitBasket[\"mango\"]=7')
fruitBasket["mango"]=7
PrintHelper.PrintCode('print(fruitBasket)')
print(fruitBasket)
PrintHelper.PrintSubtitle('Delete Item From Dictionary')
PrintHelper.PrintCode('fruitBasket={\"apple\":3,\"banana\":5,\"cherry\":50}')
PrintHelper.PrintCode('print(fruitBasket)')
PrintHelper.PrintCode('del fruitBasket[\"banana\"]')
PrintHelper.PrintCode('print(fruitBasket)')
fruitBasket={"apple":3,"banana":5,"cherry":50}
print(fruitBasket)
del fruitBasket["banana"]
print(fruitBasket)
PrintHelper.PrintTitle('Dictionary Methods')
PrintHelper.PrintSubtitle('copy()')
PrintHelper.PrintCode('fruitBasket={\"apple\":3,\"banana\":5,\"cherry\":50}')
PrintHelper.PrintCode('fruitBasketAlias=fruitBasket')
PrintHelper.PrintCode('fruitBasketCopy=fruitBasket.copy()')
PrintHelper.PrintCode('print(id(fruitBasket))')
PrintHelper.PrintCode('print(id(fruitBasketAlias))')
PrintHelper.PrintCode('print(id(fruitBasketCopy))')
fruitBasket={"apple":3,"banana":5,"cherry":50}
fruitBasketAlias=fruitBasket
fruitBasketCopy=fruitBasket.copy()
print(id(fruitBasket))
print(id(fruitBasketAlias))
print(id(fruitBasketCopy))
PrintHelper.PrintSubtitle('keys()')
PrintHelper.PrintCode('print(id(fruitBasket.keys()))')
PrintHelper.PrintCode('print(id(fruitBasketAlias.keys()))')
PrintHelper.PrintCode('print(id(fruitBasketCopy.keys()))')
print(id(fruitBasket.keys()))
print(id(fruitBasketAlias.keys()))
print(id(fruitBasketCopy.keys()))
PrintHelper.PrintSubtitle('values()')
PrintHelper.PrintCode('print(id(fruitBasket.values()))')
PrintHelper.PrintCode('print(id(fruitBasketAlias.values()))')
PrintHelper.PrintCode('print(id(fruitBasketCopy.values()))')
print(id(fruitBasket.values()))
print(id(fruitBasketAlias.values()))
print(id(fruitBasketCopy.values()))
PrintHelper.PrintSubtitle('items()')
PrintHelper.PrintCode('print(id(fruitBasket.items()))')
PrintHelper.PrintCode('print(id(fruitBasketAlias.items()))')
PrintHelper.PrintCode('print(id(fruitBasketCopy.items()))')
print(id(fruitBasket.items()))
print(id(fruitBasketAlias.items()))
print(id(fruitBasketCopy.items()))
PrintHelper.PrintSubtitle('type of them')
PrintHelper.PrintCode('print(type(fruitBasket.keys()))')
PrintHelper.PrintCode('print(type(fruitBasket.values()))')
PrintHelper.PrintCode('print(type(fruitBasket.items()))')
print(type(fruitBasket.keys()))
print(type(fruitBasket.values()))
print(type(fruitBasket.items()))
PrintHelper.PrintSubtitle('get()')
PrintHelper.PrintCode('apple=fruitBasket.get(\"apple\")')
PrintHelper.PrintCode('if apple:')
PrintHelper.PrintCode('    print(\"apple is in the basket\")')
PrintHelper.PrintCode('else:')
PrintHelper.PrintCode('    print(\"no orange in the basket\")')
PrintHelper.PrintCode('print(apple)')
apple=fruitBasket.get("apple")
if apple:
    print("apple is in the basket")
else:
    print("no orange in the basket")
print(apple)
PrintHelper.PrintTitle('keys should be immutable data type')
PrintHelper.PrintSubtitle('string')
PrintHelper.PrintCode('t={\"apple\":1}')
t={"apple":1}
PrintHelper.PrintCode('print(t.get(\"apple\"))')
print(t.get("apple"))
PrintHelper.PrintSubtitle('integer')
PrintHelper.PrintCode('t={1:1}')
t={1:1}
PrintHelper.PrintCode('print(t.get(1))')
print(t.get(1))
PrintHelper.PrintSubtitle('float')
PrintHelper.PrintCode('t={1.0:\"apple\"}')
t={1.0:"apple"}
PrintHelper.PrintCode('print(t.get(1.0))')
print(t.get(1.0))
PrintHelper.PrintSubtitle('tuple')
PrintHelper.PrintCode('t={(1,2,\"apple\"):12}')
t={(1,2,"apple"):12}
PrintHelper.PrintCode('print(t.get((1,2,\"apple\")))')
print(t.get((1,2,"apple")))
PrintHelper.PrintTitle('Storing complicated values')
print('略')
PrintHelper.PrintTitle('Lookup Speed')
PrintHelper.PrintSubtitle('List Lookup Sample')
PrintHelper.PrintCode('from datetime import datetime')
PrintHelper.PrintCode('numlist=[x for x in range(1,8000)]')
PrintHelper.PrintCode('start=datetime.now()')
PrintHelper.PrintCode('count=0')
PrintHelper.PrintCode('for i in range(5000,10000):')
PrintHelper.PrintCode('    if i in numlist:')
PrintHelper.PrintCode('        count+=1')
PrintHelper.PrintCode('end=datetime.now()')
PrintHelper.PrintCode('print(\"{}.{} seconds needed to find {} numbers\".format(')
PrintHelper.PrintCode('    (end-start).seconds,(end-start).microseconds,count))')
from datetime import datetime
numlist=[x for x in range(1,8000)]
start=datetime.now()
count=0
for i in range(5000,10000):
    if i in numlist:
        count+=1
end=datetime.now()
print("{}.{} seconds needed to find {} numbers".format(
    (end-start).seconds,(end-start).microseconds,count))
PrintHelper.PrintSubtitle('Dictionary Lookup Sample')
PrintHelper.PrintCode('numlist={x:x for x in range(1,8000)}')
PrintHelper.PrintCode('start=datetime.now()')
PrintHelper.PrintCode('count=0')
PrintHelper.PrintCode('for i in range(5000,10000):')
PrintHelper.PrintCode('    if i in numlist:')
PrintHelper.PrintCode('        count+=1')
PrintHelper.PrintCode('end=datetime.now()')
PrintHelper.PrintCode('print(\"{}.{} seconds needed to find {} numbers\".format(')
PrintHelper.PrintCode('    (end-start).seconds,(end-start).microseconds,count))')
numlist={x:x for x in range(1,8000)}
start=datetime.now()
count=0
for i in range(5000,10000):
    if i in numlist:
        count+=1
end=datetime.now()
print("{}.{} seconds needed to find {} numbers".format(
    (end-start).seconds,(end-start).microseconds,count))

