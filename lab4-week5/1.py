def zhishu(number):
    if number>1:
        for i in range(2,number):
            if number%i == 0:
                return False
            
        return True
    else:
        return False

number = int(input("请输入一个数"))
if zhishu(number):
    print("是质数")
else:
    print("不是质数")