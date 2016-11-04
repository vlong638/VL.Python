def factorial():
    total = 1
    for i in range( 1, 11 ):
        total *= i
        yield total
    
fseq = factorial()
print(type(fseq))
for n in fseq:
    print( n, end=" " )
