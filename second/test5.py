import numpy as np
rng = np.random.default_rng()
a=rng.integers(10,size=8)

print("a:",a)

print("a[-1]:",a[-1])
print("a[2]:",a[2])


print("a[2:5]:",a[2:5])
print("a[:2]:",a[:2])
print("a[5:]:", a[5:])

print("for循环遍历结果:")
for x in a:
    print(x,end='',)
print('\n')
print("np.nditer遍历结果:")
for i in np.nditer(a):
    print(i,end='')