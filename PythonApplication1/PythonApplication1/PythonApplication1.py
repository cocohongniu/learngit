from math import radians
from tkinter import END

import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt




#生成一个冒泡排序函数
def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num





def main():
    num1 = 11
    num2 = 2345
    #str1 = "我是要拼接%s和%s" % (num1, num2)
    print("我是要拼接%s和%s" % (num1, num2))



main()

