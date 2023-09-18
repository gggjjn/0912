#写一个python程序，给定一个常数n(n>0),求n的阶乘。
n = int(input("请输入一个正整数 n: "))
m = 1
if n < 0:
    print("输入必须为正整数")
elif n == 0:
    print(f"{n} 的阶乘是 1")
else:
    for i in range(1, n + 1):
        m *= i
    print(f"{n} 的阶乘是 {m}")
