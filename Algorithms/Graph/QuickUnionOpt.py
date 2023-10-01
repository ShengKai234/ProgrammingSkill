class QuickUnion():

    def __init__(self, size):
        self.rootArray = [i for i in range(size)]
    def find(self, v):
        if v == self.rootArray[v]:
            return v
        self.rootArray[v] = self.find(self.rootArray[v])
        return self.rootArray[v]
    
    def union(self, x, y):
        rootX = self.find(x) # as head
        rootY = self.find(y)
        if rootX != rootY:
            self.rootArray[rootY] = rootX
    
    def connected(self, x,  y):
        return self.find(x) == self.find(y) 

# Test Case
uf = QuickUnion(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 0) 
uf.union(2, 1)
uf.union(3, 2)
uf.union(4, 3)
uf.union(5, 4)
uf.union(6, 5)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(7, 6)
print(uf.connected(4, 9))  # true
print(uf.rootArray)
