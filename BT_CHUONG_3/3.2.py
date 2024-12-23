import numpy as np

arr = np.arange(10)
print("Array ban đầu (arr) là:", arr)
print("Kiểu dữ liệu của arr là:", arr.dtype)
print("Kích thước của arr là:", arr.shape)

arr_le = arr[arr % 2 != 0]  
arr_chan = arr[arr % 2 == 0]  
print("Các phần tử lẻ trong arr là:", arr_le)
print("Các phần tử chẵn trong arr là:", arr_chan)

arr_update_1 = np.where(arr % 2 == 0, arr, -1)  
print("Array sau khi cập nhật (arr_update_1):", arr_update_1)