# 二分查找的 Python 实现

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # 如果中间值就是目标值
        if arr[mid] == target:
            return mid
        
        # 如果目标值比中间值大，继续在右半部分查找
        elif arr[mid] < target:
            left = mid + 1
        
        # 如果目标值比中间值小，继续在左半部分查找
        else:
            right = mid - 1
    
    # 如果没有找到目标值，返回 -1
    return -1

# 测试代码
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14

result = binary_search(arr, target)

if result != -1:
    print(f"目标值 {target} 位于索引 {result}.")
else:
    print(f"目标值 {target} 不在数组中.")
