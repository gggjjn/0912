import re

def validate_id_card(id_card):
    # 定义身份证号的正则表达式
    pattern = r'^[1-9]\d{5}(19\d{2}|20[0-2]\d)(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}([0-9]|X)$'
    
    # 使用正则表达式匹配身份证号
    if re.match(pattern, id_card):
        return True
    else:
        return False

# 测试身份证号是否合法
id_card1 = "110101199003077473"  # 合法的身份证号
id_card2 = "123456789012345678"  # 不合法的身份证号

if validate_id_card(id_card1):
    print(f"{id_card1} 是合法的身份证号")
else:
    print(f"{id_card1} 不是合法的身份证号")

if validate_id_card(id_card2):
    print(f"{id_card2} 是合法的身份证号")
else:
    print(f"{id_card2} 不是合法的身份证号")
