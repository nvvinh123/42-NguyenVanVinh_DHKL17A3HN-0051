import numpy as np

arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1  
print("arr_zeros:", arr_zeros)

arr_h = np.arange(10, 25)
print("arr_h ban đầu:", arr_h)
arr_h_dao_nguoc = arr_h[::-1]
print("arr_h đảo ngược:", arr_h_dao_nguoc)

arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
print("arr_k:", arr_k)
arr_1 = arr_k[arr_k != 0]
print("arr_1:", arr_1)

arr_2 = np.append(arr_1, [10, 20])
print("arr_2:", arr_2)

arr_3 = np.insert(arr_2, 5, 100)
print("arr_3:", arr_3)

arr_4 = np.delete(arr_3, [0, 1, 2])
print("arr_4:", arr_4)