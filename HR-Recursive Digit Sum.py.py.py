def superDigit(n, k):
    if len(n) == 1:
        return n
        
    new = 0
    for i in n:
        new += int(i)
    
    new = new * k
    
    return superDigit(str(new), 1)
