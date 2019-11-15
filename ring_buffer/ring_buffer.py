class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    #increment self.current by 1 and then divide by self.capacity to make sure capacity isn't exceeded
    self.current = (self.current + 1) % self.capacity
   


  def get(self):
      #set the variable storage to self.storage
      storage = self.storage
      #set variable items to be self.storage after filtering out all the None items
      items = list(filter(None, storage))
      #return the filtered list
      return items