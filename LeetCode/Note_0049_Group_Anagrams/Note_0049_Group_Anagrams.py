from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        for s in strs:
            string_s = ' '.join(sorted(s))
            
            if string_s in result:
                result[string_s].append(s)
            else:
                result[string_s] = [s]

        return result.values()

    def groupAnagrams_tuple(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            string_s = tuple(sorted(s))
            print(string_s)
            if string_s in result:
                result[string_s].append(s)
            else:
                result[string_s] = [s]

        return result.values()

if __name__ == "__main__":
    print("0049")
    solution = Solution()
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs))

    print(solution.groupAnagrams_tuple(strs))
    
# T:O(K * NlogN)
# S:O(K * N)