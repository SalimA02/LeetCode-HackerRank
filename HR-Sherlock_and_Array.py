def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        if left_sum == (total_sum - left_sum - arr[i]):
            return "YES"
        left_sum += arr[i]
    
    return "NO"
