import PrintHelper
PrintHelper.PrintCode('def sortIntegers(A):')
PrintHelper.PrintCode('    i=0')
PrintHelper.PrintCode('    while i<len(A)-1:')
PrintHelper.PrintCode('       j=i+1')
PrintHelper.PrintCode('       while j<len(A):')
PrintHelper.PrintCode('           if(A[i]>A[j]):')
PrintHelper.PrintCode('               t=A[i]')
PrintHelper.PrintCode('               A[i]=A[j]')
PrintHelper.PrintCode('               A[j]=t')
PrintHelper.PrintCode('           j=j+1')
PrintHelper.PrintCode('       i=i+1')
def sortIntegers(A):
    i=0
    while i<len(A)-1:
       j=i+1
       while j<len(A):
           if(A[i]>A[j]):
               t=A[i]
               A[i]=A[j]
               A[j]=t
           j=j+1
       i=i+1

PrintHelper.PrintCode('A=[3, 2, 1, 4, 5]')
PrintHelper.PrintCode('for value in A:')
PrintHelper.PrintCode('    print(value)    ')
PrintHelper.PrintCode('print(\"\")')
A=[3, 2, 1, 4, 5]
for value in A:
    print(value)    
print("")
PrintHelper.PrintCode('sortIntegers(A)')
PrintHelper.PrintCode('print(\"\")')
PrintHelper.PrintCode('for value in A:')
PrintHelper.PrintCode('    print(value)')
sortIntegers(A)
print("")
for value in A:
    print(value)

    
        
