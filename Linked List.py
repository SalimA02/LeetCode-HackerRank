class Node:
    def __init__(self, data):
        """Initialize a node with the given data and no next node."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def add(self, item):
        """Add an item to the end of the linked list."""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, item):
        """Insert an item at a specified index in the linked list."""
        if index < 0:
            raise IndexError("Index out of bounds")
        
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def remove(self, item):
        """Remove the first occurrence of the specified item from the linked list."""
        if self.is_empty():
            raise ValueError(f"{item} not found in linked list")
        
        if self.head.data == item:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError(f"{item} not found in linked list")

    def pop(self, index=None):
        """Remove and return the item at the specified index, or the last item if no index is given."""
        if self.is_empty():
            raise IndexError("Pop from an empty linked list")
        
        if index is None:
            index = self.size() - 1
        
        if index < 0:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            item = self.head.data
            self.head = self.head.next
            return item
        
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        
        item = current.next.data
        current.next = current.next.next
        return item

    def size(self):
        """Return the number of items in the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
