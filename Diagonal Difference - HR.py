def diagonalDifference(arr):
    left = 0
    right = 0
    length = len(arr)
    
    for i in range(length):
        left += arr[i][i]
        right += arr[i][length-1-i]
    
    return abs(left - right)
