func=lambda x,y:x if x>y else y
print(func(5,6))

func=lambda x,y:x if x>y else x if x==10 else y
print(func(5,16))
print(func(10,16))
