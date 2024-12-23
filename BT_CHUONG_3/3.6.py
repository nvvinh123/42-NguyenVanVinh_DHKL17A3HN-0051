import numpy as np

# Câu 1: Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Array arr (3x3 với True):\n", arr)

# Câu 2: Tạo arr_ID và tạo array 2 chiều có kích thước 3x3 từ arr_ID
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).reshape(3, 3)
print("\nArray arr_ID (3x3):\n", arr_ID)

# Chuyển cột 1 sang cột 3 và ngược lại
arr_ID[:, [1, 2]] = arr_ID[:, [2, 1]]
print("\nArray arr_ID sau khi đổi cột 1 và cột 3:\n", arr_ID)

# Câu 3: Chuyển dòng 1 sang dòng 2 và ngược lại
arr_ID[[0, 1]] = arr_ID[[1, 0]]
print("\nArray arr_ID sau khi đổi dòng 1 và dòng 2:\n", arr_ID)

# Câu 4: Đảo ngược các dòng của arr_ID
dao_nguoc_dong = arr_ID[::-1]
print("\nArray arr_ID sau khi đảo ngược các dòng:\n", dao_nguoc_dong)

# Câu 5: Đảo ngược các cột của arr_ID
dao_nguoc_cot = dao_nguoc_dong[:, ::-1]
print("\nArray arr_ID sau khi đảo ngược các cột:\n", dao_nguoc_cot)

# Câu 6: Kiểm tra giá trị rỗng trong arr_2D_null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
gia_tri_rong = np.isnan(arr_2D_null).any()
print("\nCó giá trị rỗng trong arr_2D_null:", gia_tri_rong)

# Câu 7: Thay thế giá trị null bằng 0
arr_2D_null_filled = np.nan_to_num(arr_2D_null, nan=0)
print("\nArray arr_2D_null sau khi thay thế NaN bằng 0:\n", arr_2D_null_filled)