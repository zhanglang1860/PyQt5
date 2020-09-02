import numpy as np

a = np.array(range(12)).reshape((3, 4)).astype("float")
print(a)
print(np.isnan(a))

a[[1], 2:] = np.nan
print(a)
print(np.isnan(a))


# lista=[]
# for i in range(0,4,2):
#     print(i)
#     lista.append(i)
# print(lista)
# b=np.array(range(10),dtype=np.bool)
print(a)
print("*" * 100)
print(a[0::2, :2])
# print(b)
# print(b.astype("i1"))
