def decimal_to_binary(decimal_num, num_places=8):
    # 判断小数是否为负数
    is_negative = decimal_num < 0
    if is_negative:
        decimal_num = abs(decimal_num)
    # 将整数部分转换为二进制
    binary_integer_str = bin(int(decimal_num))[2:]
    # 将小数部分转换为二进制
    binary_fraction = [] # 二进制小数部分初始化为空
    decimal_num -= int(decimal_num)
    for _ in range(num_places):
        decimal_num *= 2
        binary_digit = int(decimal_num)
        binary_fraction.append(str(binary_digit))
        decimal_num -= binary_digit
    
    binary_fraction_str = ''.join(binary_fraction)
    
    # 如果小数为负数，添加负号
    if is_negative:
        binary_str = "-" + binary_integer_str + "." + binary_fraction_str
    else:
        binary_str = binary_integer_str + "." + binary_fraction_str
    return binary_str
# 输入一个十进制小数
decimal_number = 10.625
# 转换并打印二进制小数表示
binary_representation = decimal_to_binary(decimal_number, num_places=8)
print(f"十进制数 {decimal_number} 的二进制表示为: {binary_representation}")
