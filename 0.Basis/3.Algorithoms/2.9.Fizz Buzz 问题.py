class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results
s=Solution()
result= s.fizzBuzz(16)
print(type(result))
print(result)
