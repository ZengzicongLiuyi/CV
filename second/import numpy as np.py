import numpy as np

data1 = [1,2,3,4,5.6]
data2 = [[1,2,3],[4,5,6]]
data3 = [[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]

arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

print("arr1.ndim:", arr1.ndim)

print("arr3.shape:", arr2.shape)
print("np.shape(arr2):" , np.shape(arr2))

print("arr3.size:", arr3.size)
print("np.size(arr3):", np.size(arr3))
print("np.size(arr3,0):", np.size(arr3,0))
print("np.size(arr3,0):", np.size(arr3,1))
print("arr3.dtype:", arr3.dtype)


