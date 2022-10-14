from curses.ascii import isdigit
from typing import List
from functools import cmp_to_key

class Solution(object):

    def recorderLogFiles(self, logs: List[str]) -> List[str]:
    
        def cmp(log1: str, log2: str):
            arr1 = list(log1.split(" ", 1))
            arr2 = list(log2.split(" ", 1))

            if not arr1[1][0].isdigit() and not arr2[1][0].isdigit():
                isEqueal = arr1[1] == arr2[1]
                if not isEqueal:
                    return -11 if arr1[1] < arr2[1] else 1
                
                return -1 if arr1[0] < arr2[0] else 1
            
            # a, b
            if arr1[1][0].isdigit() and arr2[1][0].isdigit():
                # return a == b
                return 0
            elif arr1[1][0].isdigit() and not arr2[1][0].isdigit():
                # return b < a
                return 1
            elif not arr1[1][0].isdigit() and arr2[1][0].isdigit():
                # return a < b
                return -1
            
            return 0
        logs = sorted(logs, key=cmp_to_key(cmp))
        return logs
   

if __name__ == '__main__':
    print("template")

    testCast = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    solution = Solution()
    res = solution.recorderLogFiles(testCast)
    print(res)

# T:O(nlogn)
# S:O(1)