class Solution(object):
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        size = len(gas)
        if sum(gas) < sum(cost):
            return -1
        if size == 1:
            return 0
        
        for start in range(size):
            if gas[start] <= cost[start]:
                continue
                
            i = start
            tank = gas[start]
            # print('s = ', i)
            while True:
                
                c = cost[i]
                # print(tank, c, i)
                # check fuel is enough
                if tank < c:
                    break
                
                # travel
                tank -= c

                # fix loop index
                i += 1
                if i > (size - 1):
                    i = 0

                if tank >= 0 and i == start:
                    return start
                elif i == start:
                    break

                # fill fuel
                tank += gas[i]
                # print(tank)
        return -1
   

if __name__ == '__main__':
    print("template")
    solution = Solution()

    p = 3
    n = 100
    for multiple in range(p * p, n, p):
        print(multiple)

# T:O(n)
# S:O(n)