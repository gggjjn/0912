def max_product(n):
    if n == 2:
        return 1
    if n == 3:
        return 2

    result = 1
    while n > 4:
        result *= 3
        n -= 3

    return result * n

n = 2001
result = max_product(n)
print("对于n = 2001,最大乘积为:", result)
