class Solution:
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # write you code here
        if type(nestedList) is int:
            return [nestedList]
        result=[]
        return self.subflatten(nestedList,result)

    
    def subflatten(self, source,result):
        # write you code here
        for item in source:
            if type(item) is list:
                self.subflatten(item,result)
            else:
                print("append",item)
                result.append(item)
        return result
        
s=Solution()
value=[-68,[[-97,-66],85,81,[[-63],[-71]],[-97,[166]]],[[35,136],[[125],[104]],[134,71],[154,[29]],32],[[[-2],31],164,139,[-52,[15]],[-53,25]],[-71,[[66],[139]],155,[[102],[-44]],[156,17]],[[29,-30],75,[-92,14],[1,159],76],[[133,[43]],[[-88],128],139,2,[182,[-45]]],52,[[[197],[151]],[[58],131],[[-21],[144]],[[-97],108],[147,[147]]],[[[180],[-1]],[129,[67]],[-20,-42],179,-83]];
print(type(value))
if type(value)==list:
    print(True)
result= s.flatten(value)
print(type(result))
print(result)

result= s.flatten(10)
print(type(result))
print(result)
