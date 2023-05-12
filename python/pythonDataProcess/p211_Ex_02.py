import numpy as np
from pandas import DataFrame
mydata = [[60, np.nan, 90], [np.nan, 80, 80], [40, 50, np.nan]]
myindex = ['강감찬', '김유신', '이순신']
mycolumn = ['국어', '영어', '수학']

myframe = DataFrame(data=mydata, index=myindex, columns=mycolumn)
print('\nBefore')
print(myframe)

myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].mean()

print('\nAfter')
print('-' * 60)
print(myframe)
print(myframe.describe())