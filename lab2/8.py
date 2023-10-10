import math
import random
import time
def pi_1():
    start_time=time.time()
    pi = 0
    N=10000
    for n in range(N):
        pi += ((-1)**n)/(2*n+1)
    end_time=time.time()
    run_time=end_time-start_time
    print(run_time)
    return 4*pi
def pi_2():
    start_time=time.time()
    pi=4*(4*math.atan(1/5)-math.atan(1/239))
    end_time=time.time()
    run_time=end_time-start_time
    print(run_time)
    return pi
def pi_3():
    start_time=time.time()
    n=1000000
    k=0
    for i in range(n):
        x,y=random.random(),random.random()
        dist=pow(x**2+y**2,1/2)
        if dist<=1.0:
            k+=1
    pi = 4*(k/n)
    end_time=time.time()
    run_time=end_time-start_time
    print(run_time)
    return pi
print(pi_1())
print(pi_2())
print(pi_3())