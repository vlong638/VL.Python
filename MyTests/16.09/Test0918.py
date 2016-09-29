fruitlist = ["apple", "banana", "cherry", "durian"]
newfruitlist = fruitlist
verynewfruitlist = fruitlist[:]
print( fruitlist is newfruitlist )
print( fruitlist is verynewfruitlist )
print( newfruitlist is verynewfruitlist )
for item in verynewfruitlist:
    print(item)


for i in range(1,10):
    print(i)

print(type(range(1,10)))
print(type(("apple",1,2,3)))
print(type(["apple",1,2,3]))
