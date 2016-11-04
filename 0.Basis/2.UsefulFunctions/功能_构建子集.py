def subsetsWithDup( nums):
    nums.sort()
    p = [[nums[x]
          for x in range(len(nums))
          if i>>x&1
          ]
         for i in range(2**len(nums))
         ]
    return p
result=subsetsWithDup([1,2,3])
sorted(result,reverse=False)
print(result)


#y:深度,x:宽度
def binaryList(n):
    p = [[y>>x&1
          for x in range(n)
          ]
         for y in range(2**n)
         ]
    return p
result=binaryList(3)
result.sort()
for line in result:
    print(line)
