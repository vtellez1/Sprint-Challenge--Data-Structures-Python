from collections import deque
import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid node to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # We've found a valid parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check is value is target, if so do not have to check children
        if target == self.value:
            return True
        # otherwise, target is not self.value
        else:
            # if target is less than value, check left side
            if target < self.value:
                # Have to verify there is a left child
                if self.left:
                    # Check left child with recursion
                    return self.left.contains(target)
                # If no left child, false
                else:
                    return False
            # otherwise, target is greater than value, check right side
            else:
                # HAve to verify there is a right child
                if self.right:
                    # If so, check if equals our target with recursion
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # child on most right should be the greatest number
        if self.right is None:
            # if no self.right then the parent (self.value) should be greater than any left children
            return self.value
        # if there is a right child, recursively run and keep checking until we cannot
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # Fist need to run cb on the parent
        cb(self.value)
        # If there is a left child, we need to run cb on it
        if self.left:
            self.left.for_each(cb)
        # If not left child, we do nothing
        else:
            None
        # if there is a right child, we need to run cb on it
        if self.right:
            self.right.for_each(cb)
        # If not right child, we do nothing
        else:
            None

# IN CLASS:

    def depth_first_iterative_for_each(self, cb):
        stack = []
    # add the root of the tree to the stack
        stack.append(self)
    # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
      # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
      # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack
        # breadth-first : queue
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

# DAY 2 Project -----------------------

 # Print all the values in order from low to high
 # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # Want to keep going most left and in depth because that will be lowest number
        if node.left:
            # If there is a left, recursively continue
            self.left.in_order_print(node.left)
        # Want to print value if cannot go left
        print(node.value)
        # Once printed that value, we can check right side, also recursively will check if has left or print value
        if node.right:
            self.right.in_order_print(node.right)

# Print the value of every node, starting with the given node,
# in an iterative DEPTH first traversal LIFO-Stack

    def dft_print(self, node):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

# Print the value of every node, starting with the given node,
# in an iterative BREADTH first traversal FIFO-Queue
# Goes row by row

    def bft_print(self, node):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)
