def square_root_3(c):
    g = c/2
    while(abs(g**3 - c)>0.00000000001):
        g = (2*g+c/(g**2))/3
    return g
print(square_root_3(10))
#方程为f(x)=x^3-n 迭代式为x=(x^3-n)/3*x^2