def miniMaxSum(arr):
    minimum = sum(arr) - max(arr)
    maximum = sum(arr) - min(arr)
    
    print(minimum, maximum)
