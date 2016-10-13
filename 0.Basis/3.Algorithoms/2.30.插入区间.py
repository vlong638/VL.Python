"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        # write you code here
        if len(intervals)==0:
            return [newInterval];
        if len(newInterval)==0:
            return intervals;
        result=[]
        currentInterval=intervals.pop(0)
        while currentInterval!=None:
            if newInterval[1]<currentInterval[0]:
                print("append",newInterval)
                result.append(newInterval)
                newInterval=None
                break
            elif newInterval[0]>currentInterval[1]:
                print("append",currentInterval)
                result.append(currentInterval)
            else:
                newInterval=self.merge(currentInterval,newInterval)
                print("newInterval merge",newInterval)
            if len(intervals)!=0:
                 currentInterval=intervals.pop(0)
            else:
                 currentInterval=None
        if len(newInterval)>0:
            print("append",newInterval)
            result.append(newInterval)
        if len(intervals)>0:
            print("append",intervals)
            result.append(intervals)
        return result
    def merge(self, intervalA, intervalB):
        return [min(intervalA[0],intervalB[0]),max(intervalA[1],intervalB[1])]
            

        
s=Solution()
result= s.insert([[1,5]], [2,3])
print(type(result))
print(result)
