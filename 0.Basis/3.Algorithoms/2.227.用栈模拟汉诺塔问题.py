class Tower(object):
    # create three towers (i from 0 to 2)
    def __init__(self, i):
        self.disks = []
        self.index=i

	
    # Add a disk into this tower
    def add(self, d):
        self.disks.append(d);
	
    # @param {Tower} t a tower
    # Move the top disk of this tower to the top of t.
    def move_top_to(self, t):  
        if len(self.disks) > 0:
            value=self.disks.pop(0)     
            print("from {} to {} moves value:{}".format(self.index,t.index,value))
            t.disks.insert(0,value)  
        # Write your code here  
      
    # @param {int} n an integer  
    # @param {Tower} destination a tower  
    # @param {Tower} buffer a tower  
    # Move n Disks from this tower to destination by buffer tower  
    def move_disks(self, n, destination, buffer):  
        if n == 0:  
            return  
        if n==1:
            self.move_top_to(destination)            
        else:
            print("from {} to {} buffers count:{}".format(self.index,buffer.index,n-1))
            self.move_disks(n-1,buffer,destination)
            self.move_top_to(destination)
            print("from {} to {} moves count:{}".format(buffer.index,destination.index,n-1))
            buffer.move_disks(n-1,destination,self)
    def get_disks(self):
        return self.disks
    
    def displayDisk(self,disk):
        print("disk:",disk.index)
        for letter in disk.disks:
            print(letter)

"""
Your Tower object will be instantiated and called as such:
towers = [Tower(0), Tower(1), Tower(2)]
for i in xrange(n - 1, -1, -1): towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print towers[0], towers[1], towers[2]
"""


towers = [Tower(0), Tower(1), Tower(2)]
for i in range(1,4):
    towers[0].add(i)
towers[0].displayDisk(towers[0])
towers[0].displayDisk(towers[1])
towers[0].displayDisk(towers[2])
towers[0].move_disks(3, towers[2], towers[1])
towers[0].displayDisk(towers[0])
towers[0].displayDisk(towers[1])
towers[0].displayDisk(towers[2])
