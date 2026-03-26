def minFlips(s):
    n = len(s)
    
    if n % 2 != 0:
        return -1
    
    flips = 0
    
    for i in range(0, n, 2):
        if s[i] != s[i+1]:
            flips += 1
    
    return flips
