"""
设计一个算法，找出只含素因子2，3，5 的第 n 大的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

 注意事项

我们可以认为1也是一个丑数
"""
"""
 @param {int} n an integer.
 @return {int} the nth prime number as description.
"""
class Solution:
    def nthUglyNumber(self, n):
        import heapq
        if n <= 1:
            return n
        
        key = [2, 3, 5]
        h = [(1,0)]
        value,level=heapq.heappop(h)
        print("heapq.heappop",value,level)
        n -= 1
        
        for i in range(3):
            heapq.heappush(h, (key[i], i))
            print("heapq.heappush",key[i],i)

        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            print()
            print("heapq.heappop",value,level)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                print("heapq.heappush",new_value,level)
                level += 1
            n -= 1
        return value
    
    def nthUglyNumber2(self, n):
        # write your code here
        index=0
        cur=0
        x=0
        while index<n:
            while self.isUgly(x)!=True:
                x+=1
            cur=x
            x+=1
            index+=1
        return cur
 
    def isUgly(self, num):
        if num==0:
            return False
        if num==1:
            return True
        else:
            if num%2==0:
                return self.isUgly(num/2)
            if num%3==0:
                return self.isUgly(num/3)
            if num%5==0:
                return self.isUgly(num/5)
            return False
s=Solution()
import datetime
time1=datetime.datetime.now()
result= s.nthUglyNumber(10)
time2=datetime.datetime.now()
print(result,"time:",time2-time1)
"""
time3=datetime.datetime.now()
result= s.nthUglyNumber2(599)
time4=datetime.datetime.now()
print(result,"time:",time4-time3)
"""
