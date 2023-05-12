import numpy as np
import pandas as pd


filename = '과일매출현황.csv'

print('\n# 원본 데이터 프레임')
myframe = pd.read_csv(filename, index_col='과일명')
print(myframe)
print('-' * 100)

mydict = {'구입액':50, '수입량':20}
myframe.fillna(mydict, inplace=True)

print(myframe)
print('-' * 100)

print(myframe.sum(axis=0))
print('-' * 100)

print(myframe.sum(axis=1))
print('-' * 100)

print(myframe.mean(axis=0))
print('-' * 100)

print(myframe.mean(axis=1))