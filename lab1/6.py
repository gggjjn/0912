#写一个python程序，输入w,x,y,z三个数，将这三个数从大到小使用print函数打印出来
x = input("请输入第一个数：")
y = input("请输入第二个数：")
z = input("请输入第三个数：")
w = input("请输入第四个数：")
m = sorted([x,y,z,w],reverse=True)
print(m)