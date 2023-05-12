import numpy as np

a=np.array([-1,3,2,-6])
b=np.array([3,6,1,2])
A=np.reshape(a, [2,2])
B=np.reshape(b, [2,2])
print('sol 1')
print(A)
print('sol 2')
print(B)

result3_1=np.matmul(A, B)
result3_2=np.matmul(B, A)
print('sol 3_1')
print(result3_1)
print('sol 3_2')
print(result3_2)

a=np.reshape(a, [1,4])
b=np.reshape(b, [1,4])
b2 =  np.transpose(b)
print('sol 4-1')
print(b2)

result4 = np.matmul(a, b2)
print('sol 4-2')
print(result4)

