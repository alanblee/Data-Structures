"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the value of the node insert is being called on
        if value < self.value:
            # if its less than the initial node value, put value in left side
            # check to see if left has a node
            if self.left:
                # if a node is at the left, call insert on this node
                self.left.insert(value)
            else:
                # if left node is empty, create a new node instance here
                self.left = BSTNode(value)
        else:  # if node is not less than initial node value, go right
            # check to see if theres a right node
            if self.right:
                # if a node is at the right, call insert on this node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == the initial root value, return true
        if target == self.value:
            return True

        # if target is less than initial node, it will stay on the left side and check compare target against the next node
        if target < self.value:
            # check if the left value exists
            if self.left:
                # if it exists, check to see if target = the left value
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value

        if self.right:
            return self.right.get_max()
        else:
            return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize a queue
        que = deque()
        # add first node to the que
        que.append(node)

        # loop through the queue
        while len(que) > 0:
            # pop the first node out
            current_node = que.popleft()
            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize stack
        stack = []
        # append the starting node to stack
        stack.append(node)

        # loop through the stack and print the value
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
