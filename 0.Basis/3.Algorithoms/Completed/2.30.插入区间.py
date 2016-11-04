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
        #add newInterval or intervals
        while len(intervals)>0:
            if newInterval[1]<intervals[0][0]:
                result.append(newInterval)
                newInterval=None
                #print("result.append(newInterval)")
                break
            elif newInterval[0]>intervals[0][1]:
                result.append(intervals.pop(0))
                #print("result.append(intervals.pop(0))")
            else:
                newInterval=self.merge(intervals.pop(0),newInterval)
                #print("merge")
        #add intervals
        if len(intervals)>0:
            result.extend(intervals)
        #add newInterval
        if newInterval!=None:
            result.append(newInterval)
        return result
    
    def merge(self, intervalA, intervalB):
        return [min(intervalA[0],intervalB[0]),max(intervalA[1],intervalB[1])]
            

        
s=Solution()
result= s.insert([[1,5], [6,8]], [5,6])
print(result)

result= s.insert([[1,5]], [2,3])
print(result)

result= s.insert([[1,5]], [0,0])
print(result)



