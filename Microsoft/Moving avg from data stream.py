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
