# 392. Is Subsequence
## Problem
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

```
Input: s = "abc", t = "ahbgdc"
Output: true
```
Example 2:
```
Input: s = "axc", t = "ahbgdc"
Output: false
```
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

## hint
- DP
- Two pointer

## Solution
- brute force
    - Use nested for-loop to search wether the subsequence is in target
    - Complexity Analysis
        - Time Complexity: O(N^2)
        - Space Complexity: O(1)

- Recursive
    - Complexity Analysis
        - Time Complexity: O(N)
        - Space Complexity: O(N)

- Greedy