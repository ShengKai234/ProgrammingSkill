class UnionFind:
    def __init__(self):
        self.groupIdWeight = {}
        
    def find(self, nodeId):
        if nodeId not in self.groupIdWeight:
            self.groupIdWeight[nodeId] = (nodeId, 1.0)
            # {
            #     nodeId: (groupId, weight)
            # }
        
        # get group by node
        groupId, weight = self.groupIdWeight[nodeId]
        
        # find root and update, make each key is same base group
        # a/c, b/c => so a/b would be find (a/c)/(b/c) = a/b 
        if groupId != nodeId:
            newGroupId, groupWeight = self.find(groupId)
            self.groupIdWeight[nodeId] = (newGroupId, weight * groupWeight)
        return self.groupIdWeight[nodeId]
    
    def union(self, a, b, v):
        aG, aW = self.find(a)
        bG, bW = self.find(b)
        if aG != bG:
            self.groupIdWeight[aG] = (bG, bW * v / aW)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        uf = UnionFind()
        # union
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            v = values[i]
            uf.union(a, b, v)
        
        res = []
        
        for i in range(len(queries)):
            print(uf.groupIdWeight)
            a = queries[i][0]
            b = queries[i][1]
            
            if a not in uf.groupIdWeight or b not in uf.groupIdWeight:
                res.append(-1.0)
            else:
                aG, aW = uf.find(a)
                bG, bW = uf.find(b)
                
                if aG != bG:
                    res.append(-1.0)
                else:
                    res.append(aW/bW)
        return res
            


# e = [
#         ["a", "b", 2],
#         ["b", "c", 3]
#     ]

# {
#     "a": (a, 1)
# }

# {
#     "a": (a, 1)
#     "b": (b, 1)
# }

# {
#     "a": (a, 1) => (b, 1 * 2 / 1)
#     "b": (b, 1)
# }

# {
#     "a": (b, 2)
#     "b": (b, 1)
#     "c": (c, 1)
# }

# {
#     "a": (b, 2)
#     "b": (b, 1) => (c, 1 * 3 / 1)
#     "c": (c, 1)
# }

# {
#     "a": (b, 2)
#     "b": (c, 3)
#     "c": (c, 1)
# }

# all become same group, so we can use math to sovle the all query
# {
#     "a": (c, 6)
#     "b": (c, 3)
#     "c": (c, 1)
# }

# ac = 2 * 3 / 1 = 6
