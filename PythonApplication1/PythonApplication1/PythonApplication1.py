from math import radians
from tkinter import END
import time
from my import my_test as test

import numpy as np  # installed with matplotlib
import matplotlib.pyplot as plt


# 冒泡排序
def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


# 快速排序
def quick_sort(num):
    if len(num) < 2:
        return num
    else:
        pivot = num[0]
        less = [i for i in num[1:] if i <= pivot]
        greater = [i for i in num[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 比较整数的大小
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


# 生成指定的区间随机整数
def random_int(a, b):
    """
    :param a: 区间左端点
    :param b: 区间右端点
    :return: 返回一个随机整数
    """
    return np.random.randint(a, b)


def main():
    #my_test.test1()
    test.test1()
    #print("123")
main()

# print("11")
# print("22")
