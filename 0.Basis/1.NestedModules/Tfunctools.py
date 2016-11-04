from functools import reduce
def myadd(x,y):   
    return x+y

sum=reduce(myadd,(0, 1, 2, 3, 4, 5, 6))
print(sum)
sum=reduce(lambda x,y:x+y,(0, 1, 2, 3, 4, 5, 6))
print(sum)
