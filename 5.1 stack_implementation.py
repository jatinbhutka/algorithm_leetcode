# -*- coding: utf-8 -*-
"""
@author: jbhutka
"""


class Stack():
    
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
        
    
    def is_Empty(self):
        return self.stack == []
    
    def top(self):
        top = len(self.stack) - 1
        return self.stack[top]
    
    def get_stack(self):
        return self.stack
    
    def print_stack(self):
        print (s.stack)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(-1)
s.print_stack()

s.pop()
s.print_stack()
