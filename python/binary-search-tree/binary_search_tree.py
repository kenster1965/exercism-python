"""Binary Search Tree"""


class TreeNode:
    """Node of a binary search tree."""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """Return a string representation of the TreeNode."""
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    """Binary Search Tree"""
    def __init__(self, tree_data):
        """Set Binary Search Tree."""
        self.root = None
        for value in tree_data:
            self.add(value)

    def add(self, value):
        """Add a value."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        """Recursively add a value."""
        if value <= node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    def data(self):
        """Return the root node."""
        return self.root

    def sorted_data(self):
        """Returns the data."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        """Helper method for in-order traversal of the tree."""
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)
