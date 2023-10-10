import random
import math
def integrand(x):
    return x**2 + 4 * x * math.sin(x)
a = 2
b = 3
samples = 1000000
sum = 0.0
for _ in range(samples):
    x = random.uniform(a, b)
    y = integrand(x)
    sum += y
sum *= (b - a) / samples

print("定积分的估计值:", sum)
