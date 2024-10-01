def reverse(head):
    if head is None:
        return None
    
    current = head
    new_head = None
    
    while current is not None:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev
    
    return new_head
