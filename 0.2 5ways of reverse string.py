# 5 ways of reversing string

def reverseLoop(s):
    rev_s = "" 
    for c in s:
        rev_s = c + rev_s
    return rev_s


def reverseRecursion(s):
    if s == '':
        return s
    else:
        return reverseRecursion(s[1:]) + s[0]
    
    
# Using Stack:     
class stack():
    def __init__(self):
        self.stack = []
    
    def push(self, char):
        self.stack.append(char)
        
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True


def reverseStack(s):
    st = stack()
    
    for c in s:
        st.push(c)
    
    str_stack = ""
    for c in s:
        str_stack = str_stack + st.pop()
    return str_stack
    
    
def reverseExtensiveSlice(s):
    return s[::-1 ]


def reverseFunc(s):
    rst = "".join(reversed(s))
    return rst


# https://www.geeksforgeeks.org/python-reversed-function/
    # # Python code to demonstrate working of 
    # reversed() 
"""  
    # For string 
    seqString = 'geeks'
    print(list(reversed(seqString))) 
      
    # For tuple 
    seqTuple = ('g', 'e', 'e', 'k', 's') 
    print(list(reversed(seqTuple))) 
      
    # For range 
    seqRange = range(1, 5) 
    print(list(reversed(seqRange))) 
      
    # For list 
    seqList = [1, 2, 4, 3, 5] 
    print(list(reversed(seqList)))
    
    ### 
    Output :

    ['s', 'k', 'e', 'e', 'g']
    ['s', 'k', 'e', 'e', 'g']
    [4, 3, 2, 1]
    [5, 3, 4, 2, 1]
    
"""

s = "Geeksforgeeks"
  
print "The original string  is : ", s , '\n'
  
print "The reversed string(using loops) is : ", reverseLoop(s), '\n'
print "The reversed string(using Recursion) is : ", reverseRecursion(s), '\n'
print "The reversed string(using Stack) is : ", reverseStack(s), '\n'
print "The reversed string(using Extensive slice) is : ", reverseExtensiveSlice(s), '\n'
print "The reversed string(using revserse function) is : ", reverseFunc(s), '\n'
 
