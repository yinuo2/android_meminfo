# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:59:38 2017

@author: Administrator
"""

import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

filename = 'log_su/meminfo.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = row[2]
        highs.append(high)
    # print(highs)

wights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
highs_float = list(map(float, highs))

print(highs_float)

# 根据数据绘制图形

plt.figure(figsize=(11,7))
plt.plot(wights, highs_float, "bo-", linewidth=1)
#坐标轴范围
# plt.ylim(300, 400)
# plt.xlim(0, 10)

plt.xlabel('time', fontsize=16)
plt.ylabel("Number (Mb)", fontsize=16)
plt.title("meminfo", fontsize=24)

#坐标刻度
# my_y_ticks = np.arange(300, 400, 10)
# my_x_ticks = np.arange(1, 10, 1)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)
plt.yticks(range(300, 400, 10))

#展示每个坐标
for a, b in zip(wights, highs_float):
    plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=8)

# plt.show()
plt.savefig("temp.png")