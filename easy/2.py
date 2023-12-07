#here the logic i have used is first calcualte the index of the middle element in the array,
# then create a new treenode with the value of the middle elementin sorted array,
# create a new node for mid then recursivelybuild left subtree and right subtree

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class sample:
    def calculate(self, num):
   
      if not num:
          return None

      mid=len(num) // 2
      root=Node(num[mid])
      root.left=self.calculate(num[:mid])
      
      root.right=self.calculate(num[mid+1:])

      return root
      


num=[-10,-3,0,5,9]
obj=sample()
h=obj.calculate(num)
# h can be traves to get reslutant array