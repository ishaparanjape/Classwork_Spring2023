def sqrt(n):
    if n<0:
        raise ValueError("You cannot send a negative number into this function.")
    x = n
    y = 1
    
    e = .000001
    while (x-y>e):
        x = (x+y)/2
        y = n/x
    return x