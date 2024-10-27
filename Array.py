class Array:
    def __init__(self):
        """Initialize an empty array."""
        self.items = []

    def is_empty(self):
        """Check if the array is empty."""
        return len(self.items) == 0

    def add(self, item):
        """Add an item to the end of the array."""
        self.items.append(item)

    def insert(self, index, item):
        """Insert an item at a specified index in the array."""
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of bounds")
        self.items.insert(index, item)

    def remove(self, item):
        """Remove the first occurrence of the specified item."""
        if item not in self.items:
            raise ValueError(f"{item} not found in array")
        self.items.remove(item)

    def pop(self, index=None):
        """Remove and return the item at the specified index, or the last item if no index is given."""
        if self.is_empty():
            raise IndexError("Pop from an empty array")
        if index is None:
            return self.items.pop()
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items.pop(index)
