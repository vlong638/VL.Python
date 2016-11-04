import heapq
h=[]
for x in range(10,20):
    heapq.heappush(h,x)
print(heapq.heappop(h))
for x in range(0,10):
    heapq.heappush(h,x)
print(heapq.heappop(h))


h=[]
for x in range(10,20):
    heapq.heappush(h,(x,x*x))
print(heapq.heappop(h))
for x in range(0,10):
    heapq.heappush(h,(x,x*x))
print(heapq.heappop(h))
