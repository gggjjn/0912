import random
import time

# 选择排序算法
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 归并排序算法
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 生成随机数列
def generate_random_array(length):
    return [random.randint(1, 10000) for _ in range(length)]

# 测试不同长度数列的排序效果
lengths = [100, 500, 1000, 5000, 10000]

for length in lengths:
    arr = generate_random_array(length)
    
    # 复制一份待排序的数组，以便使用不同排序算法排序
    arr1 = arr.copy()
    arr2 = arr.copy()
    
    # 使用选择排序并记录时间
    start_time = time.time()
    selection_sort(arr1)
    end_time = time.time()
    selection_time = end_time - start_time
    
    # 使用归并排序并记录时间
    start_time = time.time()
    merge_sort(arr2)
    end_time = time.time()
    merge_time = end_time - start_time
    
    print(f"长度为 {length} 的数列：")
    print(f"选择排序耗时: {selection_time} 秒")
    print(f"归并排序耗时: {merge_time} 秒")
    print("="*30)
