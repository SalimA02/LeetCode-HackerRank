def reverse(llist):
    prev = None
    current = llist
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
