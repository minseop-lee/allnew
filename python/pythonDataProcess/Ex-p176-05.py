import numpy as np
from pandas import Series
from pandas import DataFrame

myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)

myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구', '마포구', '서대문구']
mylist = list(3 * onedata for onedata in range(1, 10))
myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns = mycolumns)
print ('\nDataFame + Series')
result = myframe.add(myseries, axis=0)
print(result)

myindex2 = ['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구', '마포구', '은평구']
mylist2 = list(5 * onedata for onedata in range(1, 10))
myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns = mycolumns2)

print('\nDataFame + DataFrame')
result = myframe.add (myframe2, fill_value=20)
print(result)

print('\nDataFame - DataFrame')
result = myframe.sub(myframe2, fill_value=10)
print(result)