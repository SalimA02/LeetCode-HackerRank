def lonelyinteger(a):
    unique_element = 0
    for number in a:
        unique_element ^= number
    return unique_element
