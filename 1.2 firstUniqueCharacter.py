"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # from collections import Counter
        
        cnt = collections.Counter(s)
        
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        else:
            return -1
        
        
        
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i,c in enumerate(s):
            if c not in s[:i]+s[i+1:]:
                return i
        return -1       
