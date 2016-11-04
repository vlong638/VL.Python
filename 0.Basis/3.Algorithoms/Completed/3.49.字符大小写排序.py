class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLettersByLower(self, chars):
        chars.sort(key=lambda c: c.islower())
    def sortLettersByUpper(self, chars):
        chars.sort(key=lambda c: c.isupper())
    def sortLettersByUpperWithReverse(self, chars):
        chars.sort(key=lambda c: c.isupper(),reverse=True)
s=Solution()
a=["a","b","A","c","D"]
s.sortLettersByLower(a)
print(a)
s.sortLettersByUpper(a)
print(a)
s.sortLettersByUpperWithReverse(a)
print(a)

