#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : larange_interpolation.py
# @Software: PyCharm
"""
拉格朗日插值代码处理缺省值
"""
# 导入相应模块
import pandas as pd
from  scipy.interpolate import lagrange

# 导入数据
inputfile = 'E:\python\power_leakage_identification\missing_data.xls'
# 导出处理结果
outputfile = 'E:\python\power_leakage_identification\missing_data_processed.xls'

# 读取数据
data = pd.read_excel(inputfile, header=None)

# 定义列向量为插值函数
# s为列向量，n为被插值的位置，k为取前后的数据格式，默认为5
def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    # 剔除空值
    y = y[y.notnull()]
    # 插值并返回结果
    return lagrange(y.index, list(y))(n)

# 逐个元素判断是否需要进行插值
for i in data.columns:
    for j in range(len(data)):
        # 如果为空值，则进行插值
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)

# 输出结果
data.to_excel(outputfile, header=None, index=False)