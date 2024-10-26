class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
        
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        
    def pop(self):
        """Remove and return the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()
        
    def peek(self):
        """Get the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
        
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
        
    def __str__(self):
        """Return a string representation of the stack."""
        return "Stack(" + ", ".join(map(str, reversed(self.items))) + ")"
