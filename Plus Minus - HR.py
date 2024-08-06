def plusMinus(arr):
    
    total = len(arr)
    
    zero, plus, minus = 0,0,0
    
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            plus += 1
        else:
            minus +=1
    
    zero = zero / total
    plus = plus / total
    minus = minus / total
    
    print(f"{plus:.6f}")
    print(f"{minus:.6f}")
    print(f"{zero:.6f}")
    
