#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : data_divide.py
# @Software: PyCharm
"""
将数据集划分为训练数据和测试数据，占比分别为80%和20%
"""
# 导入相应模块
import pandas as pd
# 导入随机函数shuffle,用来打乱数据
from random import shuffle

# 导入数据
datafile = 'E:/python/power_leakage_identification/model.xls'
# 读取数据
# 数据的前三列为特征，第四列为标签
data = pd.read_excel(datafile)

# 将表格转换为矩阵
data = data.as_matrix()
# 随机打乱数据
shuffle(data)

# 设置训练数据比例
# 前80%为训练数据
p = 0.8
train = data[:int(len(data)*p),:]
# 后20%为测试数据
test = data[int(len(data)*p):,:]