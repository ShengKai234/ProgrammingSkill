class UnionFind():

    def __init__(self, size):
        self.rootArray = [i for i in range(size)]

    def find(self, v):
        return self.rootArray[v]
    
    def union(self, x, y):
        rootX = self.find(x) # as head
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.rootArray)):
                if self.rootArray[i] == rootY:
                    self.rootArray[i] = rootX
    
    def connected(self, x,  y):
        return self.find(x) == self.find(y) 

# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true