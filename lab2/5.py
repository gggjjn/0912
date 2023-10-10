def square_root_3(c):
    g = c/2
    while(abs(g*g - c)>0.00000000001):
        g = (g+c/g)/2
    return g
print(square_root_3(2))
print(square_root_3(2000))