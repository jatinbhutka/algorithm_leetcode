Method 1:

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.param = []
        self.sum = 0
        self.size = size
        
    def next(self, val: int) -> float:
        self.param.append(val)
        curSize = len(self.param)
        if curSize > self.size:
            return sum(self.param[-1:-self.size-1:-1])/self.size
        self.sum += val
        movingAvg = (self.sum)/curSize
        return movingAvg
   
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)




## Method 2: This is Better Solution

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.capacity = size
        self.sum = 0
        
    def next(self, val: int) -> float:
        currSize = len(self.list)
        if currSize >= self.capacity:
            ele_pop = self.list.pop(0)
            self.sum -= ele_pop
            currSize -= 1
        self.sum += val
        currSize += 1
        movingAvg = (self.sum)/currSize
        self.list.append(val)
        return movingAvg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



#Method 3:
"""
What's need in our data structure?

Size of the moving window
queue for moving window (first in first out)
length, to determine when we are in the window where the queue is growing
total, the current total for the moving queue
We have two distinct modes: growing queue and full size queue

Growing

Append the next value
Calculate total
Increase length
Return Moving Average
Full Size

We pop/remove element 0,
Append the next value
Calculate total by subtracting element 0 and adding new value. Prevents us from having to sum the whole queue
Return Moving Average

"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size:int = size
        self.queue:int = []
        self.length:int = 0
        self.total:int = 0
        
    def next(self, val: int) -> float:
        if self.length < self.size:
            self.queue.append(val)
            self.total += val
            self.length += 1
            return self.total/self.length
        else:
            subtract = self.queue.pop(0)
            self.queue.append(val)
            self.total = self.total - subtract + val
            return self.total/self.size
