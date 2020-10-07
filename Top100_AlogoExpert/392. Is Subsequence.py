-- AlgoExpert: https://www.algoexpert.io/questions

"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""


# Method 1: By 2-Pointer

# Time: O(M)
# Space: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        ls, lt = len(s), len(t)
        
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if i == len(s):
            return True
        else:
            return False
            
            
#Method 2:

# Time: O(M + N)
def isSubsequence(self, s, t):
    remainder_of_t = iter(t)
    for letter in s:
        if letter not in remainder_of_t:
            return False
    return True


# Below One modifies Input t:
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = -1
        for cs in s:
            if cs not in t:
                return False
            else:
                t = t[t.index(cs)+1:]
        return True
            
        
