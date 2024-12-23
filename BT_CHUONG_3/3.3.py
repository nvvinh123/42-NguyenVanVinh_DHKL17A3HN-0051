import numpy as np

arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print("arr_a:",arr_a)
print("arr_b:",arr_b)
phan_tu_chung = []
for i in arr_a:
    if i in arr_b and i not in phan_tu_chung:
        phan_tu_chung.append(i)
        
arr_c = np.array(phan_tu_chung)
print("arr_c chứa các phần tử xuất hiện ở cả arr_a và arr_b là arr_c:", arr_c)              

arr_d = np.setdiff1d(arr_a, arr_b)
print("arr_d chứa các phần tử chỉ xuất hiện ở arr_a là arr_d:", arr_d)

arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
print("arr_e:",arr_e)
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("arr_f chứa các phần tử có giá trị từ 5 đến 10 của arr_e là arr_f:", arr_f)