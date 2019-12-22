"""

# 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1 :
            return False
        
        if len(s) == 0:
            return True
        
        stack = []
        
        ref = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[len(stack)-1] != ref[c]:
                    return False
                else:
                    stack.pop()
                          
        if len(stack) == 0:
            return True
                
      
