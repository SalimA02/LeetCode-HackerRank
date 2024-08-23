def minimumBribes(q):
    
    total = 0 
    n = len(q)
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
            
            
    for i in range(n):
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total += 1
    
    print(total)
