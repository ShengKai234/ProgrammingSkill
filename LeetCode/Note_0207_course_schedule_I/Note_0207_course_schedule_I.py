from typing import List

class Solution(object):
    def canFinish(self, numCourse: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        courseDict = defaultdict(list)

        for rel in prerequisites:
            nextCourse, preCourse = rel[0], rel[1]
            courseDict[preCourse].append(nextCourse)
        
        def isCyclic_backtrack(curr, courseDict, path):
            if path[curr]:
                return True

            path[curr] = True

            ret = False
            for child_course in courseDict[curr]:
                ret = isCyclic_backtrack(child_course, courseDict, path)
                if ret:
                    break
            
            path[curr] = False
            
            return ret
        
        path = [False] * numCourse
        for p in range(numCourse):
            if isCyclic_backtrack(p, courseDict, path):
                return True
        return False


# [[1, 0], [0, 1]]
# {
#     0: 1,
#     1: 0
# }
# num = 2
# path = [False, False]


if __name__ == '__main__':
    print("template")
    solution = Solution()
    res = solution.canFinish(2, [[1, 0]])
    print(res)

# T:O(n)
# S:O(n)