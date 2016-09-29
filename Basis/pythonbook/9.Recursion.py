#Fibonacci数列 递归的经典例子
import PrintHelper
PrintHelper.PrintTitle('Recursion')

def FibonacciSequence(n):
    if n<=2:
        return 1
    return FibonacciSequence(n-1)+FibonacciSequence(n-2)
print('def FibonacciSequence(n):')
print('    if n<=2:')
print('        return 1')
print('    return FibonacciSequence(n-1,n-2)')
PrintHelper.PrintCode('print(FibonacciSequence(1))')
print(FibonacciSequence(1))
PrintHelper.PrintCode('print(FibonacciSequence(2))')
print(FibonacciSequence(2))
PrintHelper.PrintCode('print(FibonacciSequence(3))')
print(FibonacciSequence(3))
PrintHelper.PrintCode('print(FibonacciSequence(4))')
print(FibonacciSequence(4))
PrintHelper.PrintCode('print(FibonacciSequence(5))')
print(FibonacciSequence(5))
