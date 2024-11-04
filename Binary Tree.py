class Node:
    """A node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """A binary tree."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.root = new_node
        else:
            self._add_recursive(self.root, new_node)

    def _add_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._add_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._add_recursive(current.right, new_node)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, current):
        result = []
        if current:
            result += self._in_order_recursive(current.left)
            result.append(current.data)
            result += self._in_order_recursive(current.right)
        return result

    def pre_order_traversal(self):
        return self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, current):
        result = []
        if current:
            result.append(current.data)
            result += self._pre_order_recursive(current.left)
            result += self._pre_order_recursive(current.right)
        return result

    def post_order_traversal(self):
        return self._post_order_recursive(self.root)

    def _post_order_recursive(self, current):
        result = []
        if current:
            result += self._post_order_recursive(current.left)
            result += self._post_order_recursive(current.right)
            result.append(current.data)
        return result
