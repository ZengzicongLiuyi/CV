import numpy as np

a = np.arange(12)
print("a",a)
print("a.shape:",a.shape)

a.shape = (2,-1)
print("用shape更改数组形状:",a)

b= np.arange(14).reshape(2,-1)
print("用reshape更改数组形状:",b)   

c= np.arange(12)
c.resize((3,4))
print("用resize更改数组形状:", c)

d= np.arange(12)
d.resize((2,3),refcheck=False)
print("用resize更改数组形状并更改元素个数:",d)

e= np.arange(12)
e.resize((3,4),refcheck=False)
print("用ravel将数组转换为一维数组，默认行优先:",np.ravel(e))
print("用ravel将数组转换为一维数组，列优先:",np.ravel(e,order = 'F'))