def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 输入两个正整数
num1 = int(input("请输入第一个正整数: "))
num2 = int(input("请输入第二个正整数: "))

# 调用函数计算最大公约数
result = gcd(num1, num2)

# 输出最大公约数
print(f"最大公约数为: {result}")
