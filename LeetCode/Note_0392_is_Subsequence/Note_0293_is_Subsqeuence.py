class Solution(object):
    # Solution 1
    def isSubsequence_recursive(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # brute force
        # for s, for t --> O(N^2)
        
        # recursive
        SOURCE_BOUND, TARGET_BOUND = len(s), len(t)
        
        def rec_isSubsquence(source_index, target_index) -> bool:
            if source_index == SOURCE_BOUND:
                # sub 先跑完
                return True
            if target_index == TARGET_BOUND:
                # target 先跑完
                return False
            
            # if s[source_index] == t[target_index]:
            #     return rec_isSubsquence(source_index + 1, target_index + 1)
            # else:
            #     return rec_isSubsquence(source_index, target_index + 1)
            
            if s[source_index] == t[target_index]:
                source_index += 1
            target_index += 1
            
            return rec_isSubsquence(source_index, target_index)
            
        return rec_isSubsquence(0, 0)
    
    # Solution 2
    def isSubsequence_two_pointer(self, s, t) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # two point
        SOURCE_BOUND, TARGET_BOUND = len(s), len(t)
        source_index, target_index = 0, 0
        while source_index < SOURCE_BOUND:
            if target_index >= TARGET_BOUND:
                return False
            if s[source_index] == t[target_index]:
                source_index += 1
            target_index += 1
            
        return True

s = "abc"
t = "ahbgdc"

solution = Solution()
assert solution.isSubsequence_recursive(s, t) == True
assert solution.isSubsequence_two_pointer(s, t) == True
print('well done, pass all test!!')