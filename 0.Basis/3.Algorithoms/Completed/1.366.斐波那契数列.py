import PrintHelper
PrintHelper.PrintCode('class Solution:')
PrintHelper.PrintCode('    # @param n: an integer')
PrintHelper.PrintCode('    # @return an integer f(n)')
PrintHelper.PrintCode('    def fibonacci(self, n):')
PrintHelper.PrintCode('        # write your code here')
PrintHelper.PrintCode('        if n==0:')
PrintHelper.PrintCode('            return 0')
PrintHelper.PrintCode('        if n==1:')
PrintHelper.PrintCode('            return 1')
PrintHelper.PrintCode('        if n>1:')
PrintHelper.PrintCode('            return self.fibonacci(n-1)+self.fibonacci(n-2)            ')
PrintHelper.PrintCode('')
PrintHelper.PrintCode('solution=Solution()')
PrintHelper.PrintCode('for i in range(10):')
PrintHelper.PrintCode('    print(i,solution.fibonacci(i))')
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n==0:
            return 0
        if n==1:
            return 1
        if n>1:
            return self.fibonacci(n-1)+self.fibonacci(n-2)            

solution=Solution()
for i in range(10):
    print(i,solution.fibonacci(i))
