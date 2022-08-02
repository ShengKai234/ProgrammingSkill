# 21. Is Subsequence
## Problem

 

Example 1:

```

```
Example 2:
```

```
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

## hint
- DP
- Two pointer

## Solution
- Iterate
    - Use nested for-loop to search wether the subsequence is in target
    - Complexity Analysis
        - Time Complexity: O(N + M)
        - Space Complexity: O(N + M)

- Recursive
    - Complexity Analysis
        - Time Complexity: O(N + M)
        - Space Complexity: O(1)

- Greedy