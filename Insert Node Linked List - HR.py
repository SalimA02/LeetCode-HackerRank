def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(position - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    
    return head
