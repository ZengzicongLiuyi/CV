import numpy as np

a= np.arange(5)

print("a:",a)
print("a+5",a+5)
print("a-5:",a-5)
print("a*5:",a*5)
print("a**2:", a**2)
print("a/2:",a/2)
print("a//2:",a//2)
print("a<2.5:",a<2.5)

b= np.array([[1,2],[3,4]])
c=np.array([[10,0],[0,10]])

print("b+c:",b+c)
print("c-b",c-b)
print("b*c",b*c)
print("b@c",b@c)
print("b.dot(c)",b.dot(c))

d= np.array([[1,2,3],[4,5,6]])
print("d.T:",d.T)

e = np.array([[1,2],[3,4]])
e+=10
print("e+=10:",e)
e*=2
print("e*=2",e)

f= np.array([[1,2,3],[4,5,6]])
print("f.min():",f.min())
print("f.max():",f.max())
print("f.sum():",f.sum())

print("f.max(axis=0):",f.max(axis=0))
print("f.max(axis=1):",f.max(axis=1))
print("f.sum(axis=0):",f.sum(axis=0))
print("f.sum(axis=1):",f.sum(axis=1))