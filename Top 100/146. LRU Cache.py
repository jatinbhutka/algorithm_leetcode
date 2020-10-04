# Method 1:
# Dict + Double LinkedList

For example:
"""
A simple dictionary lookup Operation can be done by either :

if key in d:
or
if dict.get(key)

The first has a time complexity of O(N) and the latter has O(1) which can create a lot of difference in nested statements.
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = dict()
        
    def put(self,key, value):
        if self.dic.get(key):
            self.remove(self.dic[key])
        new_node = Node(key,value)
        self.dic[key] = new_node
        self.add(new_node)
        if len(self.dic) > self.capacity:
            new_node = self.head.next
            self.remove(new_node)
            del self.dic[new_node.key]
    
    def get(self, key):
        if self.dic.get(key):
            n = self.dic[key]
            self.remove(n)
            self.add(n)
            return n.value
        return -1
    
    def add(self,node):
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self,node):
        temp_next = node.next
        temp_prev = node.prev
        temp_prev.next = temp_next
        temp_next.prev = temp_prev        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
