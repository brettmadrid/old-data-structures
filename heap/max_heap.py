class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    # store what's at the front
    # put the smallest value at the front, then remove it from our storage
    # call sift down
    # return value

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    ## while index greater than 0
    ## get the parent (index - 1) // 2
    ## if child is greater than parent--> comparator(child, parent)
    ## swap them
    ## if not, then we're still inside the while loop, but we have nothing to do
    ## break

  def _sift_down(self, index):
    ## while index is less than max index
    ## look at both children, choose the biggest
    ## left child: 2 * index, + 1
    ## right child: 2 * index, + 2
    ## swap with that child, if the chosen one is larger, update the index to the new location
    ## otherwise break out out of your loop
