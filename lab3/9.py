def construct_array(A):
    n = len(A)
    
    # 初始化左侧乘积和右侧乘积数组
    left_product = [1] * n
    right_product = [1] * n
    
    # 计算左侧乘积
    left = 1
    for i in range(1, n):
        left *= A[i-1]
        left_product[i] = left
    
    # 计算右侧乘积
    right = 1
    for i in range(n-2, -1, -1):
        right *= A[i+1]
        right_product[i] = right
    
    # 构建结果数组
    B = [left_product[i] * right_product[i] for i in range(n)]
    
    return B

# 示例用法
A = [1, 2, 3, 4]
B = construct_array(A)
print(B)  # 输出: [24, 12, 8, 6]
