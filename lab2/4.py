def square_root_1(c):
    g = 0
    for j in range(0,c+1):
        if(j*j>c and g == 0):
            g = j - 1
            break
    while(abs(g*g - c)>0.0001):
        g += 0.00001
    return g
print(square_root_1(2))