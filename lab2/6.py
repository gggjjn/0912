def square_root_31(c):
    g = c
    while(abs(g*g - c)>0.00000000001):
        g = (g+c/g)/2
    return g
def square_root_32(c):
    g = c/4
    while(abs(g*g - c)>0.00000000001):
        g = (g+c/g)/2
    return g
print(square_root_31(2))
print(square_root_32(2))