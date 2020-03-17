
# There are three implementations of a circular buffer.
# The first and second ones are more efficient because they don't change the indexes, but change values.
# The third one has a simple implementation but because of work with indexes, it's less efficient.


class FifoFirst(object):
    """
   Circular Buffer with overwriting the data when it's full
   """
 
    def __init__(self, max_len=7):
        self.max_len = max_len
        self.data = [None] * self.max_len
        self.first_value = 0
        self.last_value = 0
        self.size = 0
 
 
    def __repr__(self):
        return repr(self.data)
 
    def add(self, value):
        """
       The function adds an element in the array
       and overwrites the data if the array is full
       """
        if self.size >= self.max_len:
            self.last_value %= self.max_len
            self.first_value = (self.last_value + 1) % self.max_len
 
        self.data[self.last_value] = value
        self.last_value = (self.last_value + 1) % self.max_len
        self.size += 1
 
        return self
 
    def get(self):
        """
       The function removes the oldest element from the array
       """
        if self.size == 0:
            raise Exception("There is no value in the array")
 
        value = self.data[self.first_value]
        self.data[self.first_value] = None
        self.first_value = (self.first_value + 1) % self.max_len
        self.size -= 1
        return value
 
 
 
class FifoSecond(FifoFirst):
    """
   Circular Buffer prevents overwriting the data
   """
    def add(self, value):
        """
       The function adds an element in the array
       if the array is not full
       """
        if self.size < self.max_len:
            self.data[self.last_value] = value
            self.last_value = (self.last_value + 1) % self.max_len
            self.size += 1
            return self
        else:
            raise Exception("The queue is full")
 

class FifoWithPop(object):
 
    def __init__(self, max_len):
        self.max_len = max_len
        self.data = []
        self.size = 0
 
    def __repr__(self):
        return repr(self.data)
 
    def append(self, value):
        if self.size <= self.max_len:
            self.data.append(value)
            self.size += 1
        else:
            raise Exception("The queue is full")
 
 
    def get(self):
        if len(self.data) > 0:
            self.size -= 1
            return self.data.pop(0)
        else:
            raise Exception("The queue is empty")