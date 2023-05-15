import pandas as pd

afile = 'data03.csv'
bfile = 'data04.csv'

atable = pd.read_csv(afile, header=0, encoding='utf-8')
btable = pd.read_csv(bfile, header=None, encoding='utf-8', names=['이름','성별','국어','영어','수학'])

print(atable)
print('-' * 40)
print(btable)
print('-' * 40)

atable['반'] = '1반'
btable['반'] = '2반'

mylist = []
mylist.append(atable)
mylist.append(btable)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
print(result)
filename = 'result.csv'
result.to_csv(filename, encoding='utf-8')
print(filename + ' saved...')