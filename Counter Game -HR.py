def counterGame(n):
    moves = 0
    
    while n > 1:
        if (n & (n - 1)) == 0:
            n //= 2
        else:
            n -= 2 ** (n.bit_length() - 1)
        
        moves += 1
    
    if moves % 2 == 0:
        return "Richard"
    else:
        return "Louise"
