class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      node = BinarySearchTree(value)
      # if value is less than self.value
          if value < self.value:
              if self.left is None:
                  self.left = new BinarySearchTree(value)
              else:
                  self.left.insert(value)
          else:
              if self.right is None:
                  self.right = new BinarySearchTree(value)
              else:
                  self.right.insert(value)
      # check if left is none
      # if so, set left to be this node
      # if not, call the left node's insert with this value
​
      # if value is greater than or equal self.value
      # check if right is none
      # if it is none, set right to be a node
      # if it has a node, call self.right.insert with this value
​
  def contains(self, target):
      # if self.value is the target,
      # return True
      if self.value == target:
          return True
      else:
          if target < self.value:
              if self.left is None:
                  return False
              else:
                  return self.left.contains(target)
          else:
              if self.right is None:
                  return False
              else:
                  return self.right.contains(target)

      # if the target is less than self.value,
      # check if we have a left
      # if so return left.contains on the target
      # if not return False
​
      # otherwise the target must be greater than self.value
      # check if we have a right
      # if so, return self.right.contains on the target
      # if not, return False
​
  def get_max(self):
      # if we have a right
      if self.right is None:
          return self.value
      else:
          return self.right.get_max()
      # return right's get max
      # otherwise, return self.value
​
  def for_each(self, cb):
      # call the callback on the self's value
      cb(self.value)
​
      # if self.right
      # call rightie's for_each with the cb
  if self.right is not None:
      self.right.for_each(cb)
​
  # if self.left
  # leftie's for_each with the cb
  if self.left is not None:
      self.left.for_each(cb)
