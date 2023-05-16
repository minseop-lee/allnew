from bs4 import BeautifulSoup
from pandas import DataFrame as df
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'


html = open('ex5-10.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')

result = []
tbody = soup.find('tbody')
tds = tbody.findAll('td')
for data in tds:
    result.append(data.text)

print(result)
print('-' * 100)

mycolumns=['이름', '국어', '영어']

myframe = df(np.reshape(np.array(result),(4,3)), columns=mycolumns)
myframe = myframe.set_index('이름')

print(myframe)
print('-' * 100)

myframe.astype(float).plot(kind='line', rot=0, title='score', legend=True)

filename = 'scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
print('-' * 100)
plt.show()





