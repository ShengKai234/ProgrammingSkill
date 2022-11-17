class Solution(object):
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(q, level):
            if level == k:
                return
            
            for i in range(len(q)):
                tmp = q[i]
                if tmp == 0:
                    q.append(0)
                    q.append(1)
                else:
                    q.append(1)
                    q.append(0)
            rec(q, level + 1)
        
        q = [0]
        rec(q, 1)
        return q[k - 1]
   

if __name__ == '__main__':
    print("template")
    solution = Solution()
    print(solution.kthGrammar(30, 0))

# T:O(n)
# S:O(n)