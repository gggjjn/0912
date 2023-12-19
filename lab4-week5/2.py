import time

start_time = time.time()

# 在这里执行你的程序
#例子:使用for循环计算1到100的和
sum = 0
for i in range(1,101):
    sum += i
print("1到100的和是:", sum)

end_time = time.time()
execution_time = end_time - start_time
print(f"程序执行时间：{execution_time} 秒")