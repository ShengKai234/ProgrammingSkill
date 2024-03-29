class UnionFindRank:

    def __init__(self, size):
        self.arr = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        while x != self.arr[x]:
            x = self.arr[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.arr[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.arr[rootX] = rootY
            else:
                self.arr[rootX] = rootY
                self.rank[rootY] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFindRank(10)
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