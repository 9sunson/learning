import numpy as np
from collections import Counter


def counter(arr):
    """获取每个元素的出现次数，使用标准库collections中的Counter方法"""
    return Counter(arr).most_common(2) # 返回出现频率最高的两个数


def single_list(arr, target):
    """获取单个元素的出现次数，使用list中的count方法"""
    return arr.count(target)


def all_list(arr):
    """获取所有元素的出现次数，使用list中的count方法"""
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


def single_np(arr, target):
    """获取单个元素的出现次数，使用Numpy"""
    arr = np.array(arr)
    mask = (arr == target)
    arr_new = arr[mask]
    return arr_new.size


def all_np(arr):
    """获取每个元素的出现次数，使用Numpy"""
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 3, 2, 1, 0, 2]
    print(counter(array))
    print(single_list(array, 2))
    print(all_list(array))
    print(single_np(array, 2))
    print(all_np(array))