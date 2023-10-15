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
#所求的正整数列是667个3
#对于大于五的数，乘积最大的情况是将n分成若干个3和2的和
#n%3为0则分为n/3个3，为1则分为（n-4）/3个3和2个2，为2则分成（n-2）/3个3和1个2